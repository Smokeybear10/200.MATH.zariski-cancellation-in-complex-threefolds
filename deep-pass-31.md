# Minimum horizontal degree and the ambient-lifting gap

Private research continuation, September 13, 2026.

The canonical model now has an exact minimum over **all** horizontal
actions fixing its distinguished variable: the minimum degree is one,
not the degree-two minimum of the previously restricted family.
The surface branch also closes a precise question: conditional on any
hypersurface presentation, every classified additive action lifts to
an equation-preserving polynomial derivation, and hence to every
finite equation-adic thickening. This does not yet produce an ambient
additive action.

The corrected complex threefold cancellation problem remains
\[
A[s]\simeq\mathbb C^{[4]}
\quad\Longrightarrow\quad A\simeq\mathbb C^{[3]}.
\tag{1}
\]
It is not solved here. Luo has not confirmed either the correction
of the pasted dimension or the complex-field interpretation.
This report makes no novelty, human-review or formal-verification claim.

## 1. The canonical minimum, with its full quantifier

The established polynomial ring and vertical action are
\[
B=\mathbb C[x,\lambda,w,z],\quad v=1+\lambda x,\qquad
\Delta=x^2\partial_w+2v^2w\partial_z.
\tag{2}
\]
Let \(\mathcal H_x\) be all LNDs \(\delta\) of \(B\) satisfying
\(\delta x=0,\ \delta\lambda=1\). Because \(\lambda\) is already
an ambient coordinate, finite slice projection gives actual coordinates
\(B=\mathbb C[x,b,c][\lambda]\) with \(\delta=\partial_\lambda\).
Write \(q(\delta)\) for the degree in \(\lambda\) of \(\Delta\)
in this frame. Equivalently it is the largest \(q\) with
\((\operatorname{ad}\delta)^q\Delta\ne0\). The result is
\[
\min_{\delta\in\mathcal H_x}q(\delta)=1.
\tag{3}
\]

The upper bound has a complete polynomial inverse:
\[
\delta_*=\partial_\lambda+2\lambda w^2\partial_z,\qquad
b=w,\quad c=z-\lambda^2w^2,\qquad
w=b,\quad z=c+\lambda^2b^2.
\tag{4}
\]
Then \(\Delta b=x^2\) and \(\Delta c=2b+4\lambda xb\).
Its top coefficient is \(4xb\partial_c\), with sliced primitive
part \(\partial_c\). The coefficient itself is not sliced.

Here is the unrestricted lower bound. Direct localization at \(x\)
and contraction give
\[
\ker\Delta=\mathbb C[x,\lambda,I],\qquad
I=x^2z-v^2w^2.
\tag{5}
\]
The contraction uses injectivity of \(I\mapsto-w^2\) modulo \(x\)
to exclude a highest pole. If \(q=0\), then \(\delta\) commutes
with \(\Delta\). Thus \(\beta=\delta w\) and \(g=\delta I\)
belong to this kernel, and
\[
g=x^2\delta z-2xv w^2-2v^2w\beta.
\tag{6}
\]
Modulo \(x\), even and odd powers of \(w\) force
\(\beta=x\beta_1,\ g=xg_1\). Divide by \(x\) and reduce again.
The same parity argument gives \(\beta_1\bmod x=0\) and
\(g_1\bmod x=2I\).

But the restriction of \(\delta\) to
\(\mathbb C(x)[\lambda,I]\) is the LND
\(\partial_\lambda+g\partial_I\). Such an LND must have \(g\)
independent of \(I\): degree at least two in \(I\) produces
strictly increasing nonzero iterate degrees; degree one with
nonzero slope produces coefficients \(a_{j+1}=a_j'+Aa_j\),
whose leading terms never vanish. Hence \(g_1\) is independent
of \(I\), contradicting its residue \(2I\). This excludes zero
for the full family, without a plane-preservation assumption.

There is also a complete minimizer classification in the smaller
sector preserving \(\mathbb C[x,\lambda,w]\). Its normalized
coordinates are \(b=w-J(\lambda,x)\), \(c=z-K(\lambda,x,b)\),
with zero constant terms in \(\lambda\). Put \(j=[\lambda]J\).
The exact criterion is
\[
\begin{aligned}
J&\equiv\lambda j-2x\lambda^2j\pmod{x^2},\\
K&=\lambda A(x,b)+\lambda^2b^2+
       \frac{2(v^2J-\lambda j)}{x^2}\,b+C(\lambda,x),
\end{aligned}
\tag{7}
\]
where \(A\in\mathbb C[x,b]\) and
\(C\in\lambda^2\mathbb C[x,\lambda]\) are arbitrary.
The congruence makes the quotient polynomial. Substitution yields
\(\Delta c=2b+\lambda(4xb+2j-x^2A_b)\); its linear coefficient
cannot be zero because \(x^2\) does not divide \(4x\).

Every top in this triangular sector has sliced primitive part.
The choice \(J=\lambda-2x\lambda^2\),
\(K=\lambda^2b^2-6\lambda^3b-4x\lambda^4b\) has
\(\delta w\bmod x=1\). It is not tangent to the reduced fixed
locus \((x,w)\), so no gauge normalizing \(\mathbb C^*\Delta\)
moves it into the old auxiliary-plane-fixing family.

The minimum in (3) is unrestricted within \(\mathcal H_x\);
the sliced-top classification is not. It remains unproved that
every unrestricted minimizer has sliced primitive top. None of
these results constructs a horizontal action on an unknown
cancellation cylinder.
[Complete proof and coefficient classification](research/minimal-horizontal-pass31.md).

## 2. Trivial bundles do not supply additive symmetries

One consequence of (1)'s hypothesis can be made stronger:
every finite projective \(A\)-module is free, not merely stably free.
Extend it to the polynomial ring \(A[s]\), apply Quillen-Suslin,
and restrict along \(s=0\). In particular the tangent bundle is free.

This does not solve symmetry extraction. The known Koras-Russell cubic
\[
X=\{x+x^2y+z^2+t^3=0\},\qquad Y=X\times\mathbb A^1
\tag{8}
\]
is \(\mathbb A^1\)-contractible and has only trivial vector bundles,
but \(\operatorname{ML}(X)=\mathbb C[x]\). It has no tangent
frame made of LNDs. These are published facts, not discoveries
of this pass.[^1][^2]

The tangent module can even be trivialized explicitly. Put
\(a=1+2xy,\ b=x^2,\ \alpha=1-2xy,\ \beta=4y^2\).
The matrix
\[
P=
\begin{pmatrix}
\alpha&b&-2z\alpha&-3t^2\alpha\\
\beta&-a&-2z\beta&-3t^2\beta\\
0&0&1&0\\
0&0&0&1
\end{pmatrix}
\quad\text{satisfies}\quad
\nabla F\,P=(1,0,0,0),\quad\det P=-1.
\tag{9}
\]
Its last three columns form a tangent basis. Its second column
sends \(x\) to \(x^2\), whereas every LND kills \(x\).
Thus no change of tangent basis can turn all its members into LNDs.

There is a stronger cylinder control. \(X\) and \(Y\) are factorial.
On any characteristic-zero UFD, a reduced invariant fraction \(a/b\)
has \(a\mid D(a)\) and \(b\mid D(b)\) for each LND \(D\).
The LND principal-ideal property then kills both numerator and
denominator. Consequently
\(\operatorname{FML}=\operatorname{Frac}(\operatorname{ML})\)
in this factorial setting. The published result
\(\operatorname{ML}(Y)=\mathbb C\) therefore gives an open
special-automorphism orbit in \(Y\).[^2][^3]
A boundary divisor would be principal and invariant under every
additive action, contradicting the same ML value. The complement
has codimension at least two.

Nevertheless all LNDs commuting with the chosen cylinder translation
have the form
\[
D+h\partial_s,\qquad D\in\operatorname{LND}(X),\ h\in\mathbb C[X].
\tag{10}
\]
They kill \(x\) and have exact generic rank three on the fourfold,
as witnessed by \(\partial_s\),
\(x^2\partial_z-2z\partial_y\), and
\(x^2\partial_t-3t^2\partial_y\). This concerns the additive
centralizer, not its full automorphism centralizer.

Thus contractibility, free bundles, and flexibility in codimension
one on a cylinder still do not supply enough intrinsic additive
directions. We do not assert full flexibility or \(Y\simeq\mathbb A^4\).
Finite-dimensional algebraic homogeneity would be stronger: the
published transitive-radical theorem, with its contractible-case
remark, would make such a \(Y\) affine space.[^4]
[Full control, proof and source boundaries](research/contractible-symmetry-pass31.md).

## 3. The surface's infinitesimal lifting obstruction vanishes

Keep the unchanged conductor surface from passes 29 and 30.
Its normalization is
\(B_0=\mathbb C[u,y,z]/((u-1)(u-i)z-y(y-1))\),
and its conductor in \(R\) is
\((d,e)\), where \(d=u^4-1,\ e=du\).
Its singular locus is three full affine lines formed by the fixed
scaled pairings of six normalization lines. All LNDs are already
classified as \(p(u)\delta_0\), \(p\in\mathbb C u+d\mathbb C[u]\).
They kill \(d,e\) and induce the same constant translation speed
on the three singular lines.

Assume, without asserting existence, a presentation
\(R=W/(F)\), \(W=\mathbb C[X,Y,Z]\). Let
\(J_F=(F_X,F_Y,F_Z)\). A polynomial lift \(E\) of a derivation
\(D\) satisfies \(E(F)=Fg\). Changing it by \(FV\) changes \(g\)
by \(V(F)\). Therefore the exact obstruction to an
\(F\)-preserving lift is
\[
\kappa_F(D)=[g]\in (J_F:F)/J_F
                =\operatorname{Ann}_{W/J_F}(F).
\tag{11}
\]
The map from \(\operatorname{Der}_{\mathbb C}(R)\) to this module
is surjective. This is not the quotient by the extended
Jacobian ideal \((F,J_F)\).

For this particular surface, \(\kappa_F(D)=0\) for every LND,
in every hypothetical presentation. Here is the geometric reason.
For lifts \(a,b\) of \(d,e\), the ambient conductor ideal is
\(K=(F,a,b)\). Regular immersion and ordinary double crossings
give \(F\in K^2\) and a global conormal basis \(\bar a,\bar b\).
On a singular line with distinct branch labels \(r_j,r_k\), its
quadratic normal symbol is
\[
F_2=c_j(t)(\bar b-r_j\bar a)(\bar b-r_k\bar a).
\tag{12}
\]
The coefficient has no zero anywhere on a full affine line,
so \(c_j(t)\) is a nonzero constant. A lift of the classified
action acts trivially on the conormal basis and differentiates
these constants to zero. Thus \(E(F)_2=0\), forcing \(g\in K\).

Locally at each singular point the ordinary Jacobian ideal equals
the conductor ideal; at a smooth point of \(F=0\) it is the unit
ideal. Off \(F=0\), the identity \(Fg\in J_F\) already gives
\(g\in J_F\). These local statements prove \(g\in J_F\) globally.
The completion and normal-cone steps use the stated regularity
hypotheses and faithful flatness, not an assumption that
\(K=(a,b)\) globally.[^5]

Correcting \(E\) now gives \(E_0(F)=0\). The \(F\)-power filtration
shows that \(E_0\) induces an LND on every \(W/(F^N)\).
The compatible exponentials belong to
\(\varprojlim_N((W/(F^N))[s])\); a uniform polynomial degree in
the action parameter is not implied.

A further necessary condition for an ambient LND is zero divergence.
For an exact lift, preservation of the hypersurface dualizing
generator gives \(\operatorname{div}E_0=Fh\). All other exact lifts
are \(E_0+FV\), \(V(F)=0\), so the remaining class lies in
\[
\theta_F(D)=[h]\in\mathcal C_F[F],\qquad
\mathcal C_F=
 W/\operatorname{div}\{V:V(F)=0\}.
\tag{13}
\]
This is a quotient of complex vector spaces and a
\(\mathbb C[F]\)-module, not generally a \(W\)-module.
The class is killed by \(F\), and vanishes exactly when a
divergence-free exact lift exists. It is not computed here.
Even a nonzero value would exclude that ambient action lift,
not the hypersurface presentation itself.
[Full lifting and divergence proof](research/hypersurface-lifting-pass31.md).

## 4. Every finite thickening is still weaker than an ambient action

The algebraization distinction has an exact general form.
Let \(W\) be an affine domain over a characteristic-zero field
\(k\), \(F\) a nonzero prime nonunit, and \(E\) a \(k\)-linear
derivation preserving \((F)\). Assume \(D=E\bmod F\) is an LND.
Then
\[
\begin{aligned}
&E\text{ is LND on every }W/(F^N)\\
&\quad\Longleftrightarrow E\text{ is LND on }W/(F^2)\\
&\quad\Longleftrightarrow E(F)\in(F^2).
\end{aligned}
\tag{14}
\]

For necessity, write \(E(F)=Fg\). On \((F)/(F^2)\simeq W/(F)\),
the induced operator is \(T=D+\bar g\). If \(\bar g\ne0\),
then \(T^q(1)\ne0\) for every \(q\). For \(D=0\) this is
immediate. Otherwise localize to the polynomial line over
\(\operatorname{Frac}(\ker D)\). Differentiation cannot cancel
the leading power of the nonzero polynomial \(\bar g\).
This contradicts nilpotence on the class of \(F\).

For sufficiency, when \(E(F)\in(F^2)\), the induced operator on
each successive \(F\)-power quotient is exactly \(D\).
Elementwise nilpotence on the finitely many filtration pieces
gives elementwise nilpotence on \(W/(F^N)\).

Yet, in \(W=\mathbb C[f,s,z,t]\), for every integer \(a\ge1\),
\[
E=\partial_s+f^a z\partial_z,\quad F=f,\qquad
E(F)=0,\quad E(s)=1,\quad E^q(z)=f^{aq}z\ne0.
\tag{15}
\]
It passes every thickening and has a slice function, but is
not an ambient LND. The least positive nilpotence index of
\(z\bmod f^N\) is \(\lceil N/a\rceil\). There is another good
lift, \(\partial_s\); this example refutes an implication about
a chosen lift, not existence of every possible lift.

There is an exact positive gate. For \(W=k[x_1,\ldots,x_n]\),
assume the equivalent conditions (14) hold.
Let \(\nu_i(N)\) be the least positive \(q\) with
\(E^q(x_i)\in(F^N)\). Then \(E\) is globally LND if and only
if each \(\nu_i(N)\) is bounded independently of \(N\).
A bound \(L_i\) puts \(E^{L_i}(x_i)\) in every power of
\((F)\), whose intersection is zero.

Put \(d=\max(1,\max_i\deg E(x_i))\) and \(e=\deg F\).
Nonzero iterates have degree at most \(1+q(d-1)\). Therefore
a coordinate failing ambient nilpotence must satisfy, for \(d>1\),
\[
\nu_i(N)\ge\frac{Ne-1}{d-1},\qquad
\liminf_{N\to\infty}\frac{\nu_i(N)}N\ge\frac e{d-1}.
\tag{16}
\]
For \(d=1\), failure is impossible. The family (15) attains the
asymptotic lower bound. Finally, a finite exact certificate is
\[
E^{q_i}(x_i)\equiv0\pmod{F^{N_i}},
\qquad N_i e>1+q_i(d-1)
\quad\text{for every }i.
\tag{17}
\]
It forces all those iterates to be zero as polynomials.
This is a sufficient certificate, not a universal bound or
a promise that a search terminates.

Zero divergence does not close the gap either. For the irreducible
nodal equation \(F=Y^2-X^2(X+1)\), let
\(H=2Y\partial_X+(3X^2+2X)\partial_Y\).
Then \(\partial_Z+FH\) preserves \(F\), has zero divergence,
has slice \(Z\), and is LND on every \(F\)-thickening. It is
not globally LND: its iterates on \(X\) are \(F^nH^n(X)\).
Here \(H^n(X)\) never vanishes by positivity of its coefficients.
[Complete uniformity and degree proof](research/finite-thickening-algebraization-pass31.md).

## 5. Verification and what remains unfinished

The three new standalone checkers contain twenty methods:
ten horizontal-minimum controls, five lifting controls, and five
finite-thickening controls. They import only unittest and SymPy.
They test exact coordinate inverses, adjoints, coefficient recovery,
parity controls, normal slopes, Jacobian corrections and iteration
identities. Universal assertions depend on the written arguments,
not extrapolation from these tests.

The full regression has **703 passing methods in 61 suites**,
including all 683 prior methods. The saved execution record is
[verification-pass-31.json](verification-pass-31.json).
Repeated runs, matrix calculations and parser controls are not
additional methods. The separate [audit record](research/proof-audits-pass31.md)
states who reconstructed which proof and which corrections were made.

The remaining obligations are distinct:

| Route | Proved here | Still required |
| --- | --- | --- |
| Canonical horizontal selection | Global minimum one; triangular-sector tops sliced | Useful selection for an unknown cylinder; unrestricted minimizer control |
| Intrinsic symmetry | Free bundles are automatic; contractible countercontrol to weak transfer | Enough compatible intrinsic additive directions from the full hypothesis |
| Candidate surface | Every action has an exact equation-preserving lift, conditional on presentation | Three generators or a presentation obstruction; ambient LND realization |
| Infinitesimal approximation | All-thickening criterion and finite positive degree certificate | A lift satisfying genuine global nilpotence |

A hypersurface embedding, an ambient LND lift, and a realization
inside the cancellation problem are separate requirements. None is
silently substituted for another. The fixed surface still has
generator number between three and four. The general proof gap is
still extracting a sufficient recognition structure from every
actual polynomial cylinder.

No submission, external contact, public priority statement or
expert-review claim is authorized or made.

[^1]: Dubouloz and Fasel, [*Families of A1-contractible affine threefolds*, Theorem 1](https://arxiv.org/pdf/1512.01933); Hoyois, Krishna and Østvær, [*A1-contractibility of Koras-Russell threefolds*, Corollary 3.7 and proof](https://content.algebraicgeometry.nl/2016-4/2016-4-019.pdf). Their hypotheses include the cubic (8). Contractibility and bundle triviality are not polynomial-cylinder isomorphisms.

[^2]: Dubouloz, [*The cylinder over the Koras-Russell cubic threefold has a trivial Makar-Limanov invariant*](https://arxiv.org/pdf/0807.4085), displayed theorem and introduction. The base invariant is credited there to Makar-Limanov. These were inherited inputs of the investigation.

[^3]: Arzhantsev, Flenner, Kaliman, Kutzschebauch and Zaidenberg, [*Flexible varieties and automorphism groups*, Propositions 4.22 and 5.1](https://arxiv.org/pdf/1011.5375), PDF pp. 30-31. Open-orbit and boundary-divisor conclusions do not assert flexibility everywhere.

[^4]: Bruce, du Plessis and Wall, *Determinacy and unipotency*, [Theorem (3.6), p. 535](https://gdz.sub.uni-goettingen.de/fulltext/PPN356556735_0088/00000541?_format=xml), and [its proof and contractible-case remark, p. 536](https://gdz.sub.uni-goettingen.de/fulltext/PPN356556735_0088/00000542?_format=xml). Together with the affine-space structure of unipotent homogeneous spaces, this supplies the stated conditional consequence.

[^5]: Stacks Project, [regular immersions and conormal criteria, Lemmas 31.22.5 and 31.22.12](https://stacks.math.columbia.edu/tag/0638), [regular sequences and the associated graded algebra, Lemma 10.69.2](https://stacks.math.columbia.edu/tag/061M), and [faithful flatness of local completion, Lemma 10.97.3](https://stacks.math.columbia.edu/tag/00MC). The nodal local calculation and its global application are given in the linked full lifting proof.
