# No invariant belongs to a generating triple of the fixed surface

For the fixed conductor-glued surface and its specified locally
nilpotent derivation, no invariant function can be one of three
algebra generators:
\[
\boxed{R\ne\mathbb C[j,a,b]\quad
       \text{for every }j\in T=\ker\partial
       \text{ and every }a,b\in R.}
\tag{1}
\]
In particular,
\[
R\ne\mathbb C[d,a,b],\qquad
R\ne\mathbb C[d(u^2-1),a,b].
\tag{2}
\]
This is a global obstruction. Both functions in (2) passed every
individual planar-fiber test in [pass 28](changed-fiber-surface-pass28.md).

The contradiction comes from the entire ambient defining polynomial,
not from monodromy alone. A hypothetical invariant-containing triple
would produce a genuine relative-plane LND on the ambient polynomial
ring. Its global kernel forces a plane base curve with at least four
branches at one point. Pulling its defining equation back to the
ambient three-space cannot produce the quadratic double crossing of
the actual surface.

The result still does not decide \(3\le\mu_{\mathbb C}(R)\le4\).
A hypothetical generating triple would have to consist entirely of
noninvariant functions for this fixed action. No ambient primitive
action, solution of cancellation, novelty or expert-review claim is made.

## 1. Fixed data and the geometric generic fiber

Use the unchanged [four-generator surface](nodal-elimination-pass23.md):
\[
B=\mathbb C[u,y,z]/(A(u)z-y(y-1)),\quad
A(u)=(u-1)(u-i),\quad d=u^4-1,
\]
\[
R=B\times_{\mathbb C[t]^6}\mathbb C[t]^3,\qquad I=dB.
\tag{3}
\]
The paired root values are \((1,i),(1,-i),(-1,i)\), with the
original split-line labels and scaled gluing parameters.

The [proved action and kernel](nodal-hypersurface-pass24.md) are
\[
\partial u=0,\quad\partial y=uA(u),\quad
\partial z=u(2y-1),\qquad
T=\mathbb C+d\mathbb C[u].
\tag{4}
\]
Also
\[
\operatorname{Frac}R=\mathbb C(u,y),\qquad
R\cap\mathbb C(u)=T.
\tag{5}
\]
At every closed point \(q\) of the three conductor lines,
\[
\widehat{\mathcal O}_{R,q}
\cong\mathbb C[[\xi,\eta,t]]/(\xi\eta).
\tag{6}
\]
These are actual properties of the fixed ring.

Take a nonconstant \(j\in T\), let \(N=\deg_u j\), and set
\[
S=\mathbb C[j],\quad K=\mathbb C(j),\quad L=\mathbb C(u).
\]
Then \(L/K\) is separable of degree \(N\). Indeed \(j(U)-J\) is
irreducible over \(\mathbb C(J)\): in \(\mathbb C[U,J]\) it is
primitive and linear in \(J\), and its degree in \(U\) is \(N\).

Let \(c_0\) be the common value of \(j\) at the four conductor roots.
The element \(j-c_0\) belongs to the conductor \(I\), so it annihilates
\(B/R\). It becomes a unit after tensoring over \(S\) with \(K\).
Consequently
\[
R_K=B_K=L[y],
\tag{7}
\]
where \(A(u)\) is a nonzero element of the field \(L\) and eliminates
\(z\). This is an equality after the specified base localization;
it does not assert \(R=B\).

If \(\overline K\) is an algebraic closure of \(K\), separability gives
\[
R\otimes_S\overline K\cong
\prod_{\sigma:L\hookrightarrow\overline K}\overline K[y].
\tag{8}
\]
Thus the geometric generic fiber is exactly a disjoint union of
\(N\) reduced affine lines.

## 2. A plane polynomial with this zero fiber has an LND Hamiltonian

We use the following elementary consequence of the
Abhyankar--Moh embedding theorem.[^am]

**Lemma.** Let \(k\) be an algebraically closed field of characteristic
zero, and \(G\in k[X,Y]\). If
\[
k[X,Y]/(G)\cong\prod_{\ell=1}^N k[t_\ell],
\tag{9}
\]
then there is a polynomial coordinate \(Q\) of \(k[X,Y]\), distinct
constants \(\alpha_\ell\), and \(c\in k^*\) such that
\[
G=c\prod_{\ell=1}^N(Q-\alpha_\ell).
\tag{10}
\]
In particular the Hamiltonian derivation
\(G_Y\partial_X-G_X\partial_Y\) is locally nilpotent, and its kernel
is \(k[Q]\).

For the proof, the quotient in (9) is reduced, so \(G\) is squarefree.
Each irreducible component is a closed embedded affine line.
Abhyankar--Moh rectifies one component to \(Q=0\), where \(Q\) is a
polynomial coordinate of the plane. On every other component the
restriction of \(Q\) has no zero, since the components are disjoint.
The only units of \(k[t]\) are nonzero constants. Hence that
restriction is a constant \(\alpha_\ell\ne0\). Its component prime
contains \(Q-\alpha_\ell\); this is itself a prime coordinate
polynomial, so the two height-one primes coincide.
The constants are distinct, proving (10).

Complete \(Q\) to polynomial coordinates \(Q,Z\), with constant
Jacobian \(\kappa\ne0\). The Hamiltonian is
\[
-\kappa c\left(\prod_\ell(Q-\alpha_\ell)\right)'
 \partial_Z.
\tag{11}
\]
This is a replica of a coordinate partial, proving the assertion.

For precision, the version of Abhyankar--Moh used here applies over
any algebraically closed characteristic-zero field, including
\(\overline{\mathbb C(j)}\). The degree-divisibility formulation
in the cited primary proof gives rectification directly:
for an embedding \(t\mapsto(f(t),g(t))\), subtract the appropriate
power of the lower-degree coordinate from the higher-degree one.
The positive degrees decrease until one coordinate is linear.
These are polynomial shears with polynomial inverses. If one
coordinate is initially constant, the other already generates \(k[t]\)
and is linear. No assertion about an arbitrary injective polynomial
map or a unit Jacobian alone is used.

## 3. A hypothetical triple produces a global ambient LND

Suppose for contradiction that \(R=\mathbb C[j,a,b]\).
Use independent ambient symbols \(J,X,Y\) and the surjection
\[
W=\mathbb C[J,X,Y]\longrightarrow R,\qquad
(J,X,Y)\longmapsto(j,a,b).
\tag{12}
\]
The kernel is a height-one prime in a UFD. Thus
\[
R=W/(F)
\tag{13}
\]
for an irreducible polynomial \(F\).
It is not a polynomial in \(J\) alone, since \(j\) is nonconstant.

Consider the actual polynomial derivation of \(W\)
\[
H=F_Y\partial_X-F_X\partial_Y,\qquad H(J)=H(F)=0.
\tag{14}
\]
By (8) and the lemma, its extension to \(\overline K[X,Y]\) is
locally nilpotent. Therefore \(H\) itself is locally nilpotent on
\(W\): for any polynomial \(w\), an iterate vanishes in the injective
extension \(W\hookrightarrow\overline K[X,Y]\), hence vanishes in \(W\).
This is descent of vanishing of actual polynomial iterates. It does
not descend an unspecified coordinate system or clear a denominator
in the defining equation.

Let \(\gamma\) be the gcd of the two coefficients of \(H\) in the UFD
\(W\), and put
\[
H=\gamma\Delta.
\tag{15}
\]
Then \(\Delta\) is a primitive polynomial \(S\)-derivation and is
locally nilpotent. Here is the elementary division argument.
If \(\Delta\gamma\ne0\), the identity
\(H\gamma=\gamma\Delta\gamma\), together with additivity of LND
degree, would imply
\[
\deg_H\gamma-1
=\deg_H\gamma+\deg_H(\Delta\gamma),
\]
which is impossible. Thus \(H\gamma=\Delta\gamma=0\), and
\(H^n(w)=\gamma^n\Delta^n(w)\). Local nilpotence of \(H\) implies
local nilpotence of \(\Delta\). Also \(\Delta(F)=0\).

The regular-sequence/comaximal criterion of
Bhatwadekar--Dutta, Theorem 4.7, now gives
\[
\ker\Delta=\mathbb C[J,P]
\quad\text{for some }P\in W.
\tag{16}
\]
Its hypotheses are satisfied globally over the Noetherian domain
\(\mathbb C[J]\). The two coefficients of \(\Delta\) are coprime
in \(W\). If their ideal is not the unit ideal, both are nonzero,
the first is a nonzerodivisor, and the second is a nonzerodivisor
modulo the first: coprimality in a UFD proves this by divisibility.
They therefore form a regular sequence. If one coefficient is zero,
the other is a unit and the comaximal case applies.[^bd]

Only the kernel assertion in that theorem is used.
There is no assumption that \(\Delta\) is fixed-point-free and
no conclusion that \(W\) is a polynomial extension of its kernel.

Since \(\Delta F=0\), equation (16) gives the **global** identity
\[
F=\Phi(J,P),\qquad \Phi\in\mathbb C[J,Z].
\tag{17}
\]
It is not an equality merely after inverting a polynomial in \(J\).
The polynomial \(\Phi\) is irreducible, because the substitution
\(\mathbb C[J,Z]\to\mathbb C[J,P]\) is injective and a nonconstant
factor there would be a nonunit factor of \(F\) in \(W\).

There is also an exact invariant restriction injection
\[
C_0:=\mathbb C[J,P]/(F)
 \cong\mathbb C[J,Z]/(\Phi)\hookrightarrow R.
\tag{18}
\]
Indeed if \(Fw\) is invariant, then \(F\Delta w=0\), so \(w\)
is invariant. Hence \((F)W\cap\ker\Delta=F\ker\Delta\).

## 4. The plane base has the full normalization field

The induced derivation \(\overline\Delta\) on \(R\) is nonzero.
Over the geometric generic fiber the Hamiltonian (11) induces a
nonzero translation on each line, since the \(\alpha_\ell\) are
distinct. Thus \(\overline H\ne0\). In particular \(\gamma\notin(F)\),
and (15) implies \(\overline\Delta\ne0\).

Any nonzero derivation of \(\operatorname{Frac}R=L(y)\) killing \(j\)
kills \(L\), because \(L/K\) is separable algebraic.
It is then a nonzero rational multiple of \(\partial_y\), whose
rational kernel is exactly \(L\) in characteristic zero.
Consequently
\[
\ker(\overline\Delta|_R)=R\cap L=T.
\tag{19}
\]
This proves the full induced invariant field and ring.
It does not assume surjectivity in (18).

Write \(p(u)=\overline P\in T\).
We next prove that the fraction field of the plane curve \(C_0\)
is all of \(L\), not a proper subfield.

Formation of the kernel of the \(S\)-linear map \(\Delta:W\to W\)
commutes with the flat base change \(S\to\overline K\). Equation (16)
therefore gives
\[
\ker\Delta_{\overline K}=\overline K[P].
\tag{20}
\]
On the other hand, \(H=\gamma\Delta\) in the domain
\(\overline K[X,Y]\), so the two derivations have the same kernel.
The lemma gives \(\ker H_{\overline K}=\overline K[Q]\).
Thus \(\overline K[P]=\overline K[Q]\).
Two generators of a one-variable polynomial algebra differ by an
affine-linear change, so \(P=\alpha Q+\beta\), \(\alpha\ne0\),
over \(\overline K\).

The geometric factorization (10) and (17) now imply
\[
\deg_Z\Phi=N.
\tag{21}
\]
Since \(\Phi\) remains irreducible over \(K\) by Gauss's lemma,
(18) gives
\[
[K(p(u)):K]=N=[L:K].
\tag{22}
\]
The inclusion \(K(p(u))\subset L\) is therefore equality.
In particular
\[
\operatorname{Frac}C_0=L=\mathbb C(u).
\tag{23}
\]

The ring \(\mathbb C[u]\) is finite over \(\mathbb C[j]\),
hence also finite over \(C_0=\mathbb C[j,p(u)]\).
Together with (23) and normality of \(\mathbb C[u]\), this proves
that \(\mathbb A^1_u\) is exactly the finite normalization of the
plane curve \(C_0\). This is the point where the full degree equality
is essential. A merely finite map of larger degree would not force
the following branch count.

## 5. Four base branches cannot pull back to the actual double crossing

Because both \(j\) and \(p\) belong to \(T\), they take constant
values \(c_0,p_0\) respectively at
\[
u=1,\quad i,\quad -1,\quad -i.
\tag{24}
\]
The four distinct normalization points therefore all lie over the
same point
\[
q_0=(J-c_0,Z-p_0)
\]
of the plane curve \(\Phi(J,Z)=0\).

A curve's branches at a complex closed point correspond to the
normalization points above it.[^branches]
Here the corresponding formal-branch statement can also be seen
directly. Complete the finite injection of the local curve ring into
its semilocal normalization. Flatness of Noetherian completion
preserves the injection, and the completed normalization is the
product of the power-series rings at its normalization preimages.
A nonzero element of the finite birational conductor has nonzero
image on every such factor; after inverting it the two rings agree.
Thus their minimal primes correspond, with at least the four factors
from (24). This justifies the formal branch count, not only the count
of points in an abstract finite cover.
Hence the formal plane germ \(\Phi(c_0+J,p_0+Z)\) has at least
four branches. Its order is at least four:
\[
\Phi(J,Z)\in(J-c_0,Z-p_0)^4.
\tag{25}
\]
This also follows by factoring the plane germ in
\(\mathbb C[[J-c_0,Z-p_0]]\): each branch contributes a nonunit
factor of order at least one. Formal curve order and factorization
are the usual plane-branch notions in the primary reference.[^am]

Choose any closed point \(q\) of an actual conductor line in
\(\operatorname{Spec}R\), and its image
\(\widetilde q\) in the hypothetical ambient three-space (12).
Then \(J-c_0\) and \(P-p_0\) both vanish at \(\widetilde q\).
Substituting into the global identity (17) gives
\[
F\in\mathfrak m_{\widetilde q}^{\,4}.
\tag{26}
\]
There are no denominators to cancel and no division by \(J-c_0\).

For completeness, the contradiction can be expressed without
appealing to a general multiplicity pullback formula.
A hypersurface germ in a smooth three-space whose defining equation
has order at least four has no quadratic relation in its associated
graded local ring. Therefore its maximal ideal \(\mathfrak m\) satisfies
\[
\dim_{\mathbb C}\mathfrak m^2/\mathfrak m^3=6,
\tag{27}
\]
the number of degree-two monomials in three variables.
For the actual completed local ring (6), the single quadratic
relation \(\xi\eta=0\) instead gives
\[
\dim_{\mathbb C}\mathfrak m^2/\mathfrak m^3=5.
\tag{28}
\]
These dimensions are preserved by completion and local-ring
isomorphism. Equations (27) and (28) contradict (13).

This proves (1) for every nonconstant invariant.
A constant invariant also cannot belong to a generating triple,
since the other two functions cannot generate a ring with
three-dimensional conductor cotangent spaces.

## 6. Consequences and limitations

The generic component count, the ambient relative LND and the
global kernel identity all matter. The argument does not infer
global embeddability from fiberwise planarity, and it does not
claim that every surface LND extends to an ambient one.
The ambient LND (14) was constructed under the much more specific
hypothesis of an invariant-containing generating triple.

In particular, any hypothetical embedding of this \(R\) into
\(\mathbb A^3\) cannot have an ambient coordinate whose restriction
is in \(T\). Every ambient polynomial coordinate system would restrict
to three noninvariant functions.

If the specified action, or a nonzero replica with the same kernel,
were to extend to an ambient LND on \(\mathbb C^{[3]}\), that LND
could not fix an ambient coordinate. Otherwise its restriction would
give the forbidden invariant-containing triple. A fixed ambient
coordinate could not restrict to a constant: then the irreducible
defining polynomial would divide that coordinate minus a constant,
making the surface a smooth plane. Thus any such extension would
have to have rank three in the usual coordinate sense.
This is only a necessary condition; rank-three LNDs are not excluded.

The original all-noninvariant generator problem remains.
The result does not decide whether a triple changing all of
\(d,e,g,h\) can generate \(R\), and the additional ambient quotient
and disconnected-plinth realization remain unproved.

## Exact controls and source boundary

A small exact control illustrates the plane-base issue:
\[
C_1=\mathbb C[d,e],\qquad
e^4=d^4(d+1),\qquad e=du.
\tag{29}
\]
Its normalization is \(\mathbb C[u]\), with \(u=e/d\) in the
fraction field and \(u^4=d+1\). The four roots in (24) lie above
the origin. Its initial plane equation is
\[
E^4-D^4=(E-D)(E+D)(E-iD)(E+iD).
\tag{30}
\]
Direct SymPy arithmetic checked the exact relation (29), the
degree-four initial form and factorization (30), and the quadratic
Hilbert counts \(6\) and \(5\). This is an illustrative control,
not the proof for the unknown polynomial \(p(u)\) in Section 4,
and these preliminary inline checks are not counted as unittest methods.

The subsequently added standalone
[exact control suite](global_invariant_embedding_checks_pass29.py)
imports only unittest and SymPy. Its seven methods additionally check
finite expansions of all four actual branches, the full quadratic
Hilbert comparison, polynomial pullback versus invalid denominator
cancellation, a nonlinear split Hamiltonian and its primitive division,
and failures when squarefreeness or disjointness is removed. These are
finite illustrative controls, not tests of the unknown \(p(u)\) or
replacements for the universal geometric proof.
The targeted run passed all seven methods in 0.381 seconds.

~~~sh
/opt/anaconda3/bin/python research/global_invariant_embedding_checks_pass29.py
~~~

The proof uses established Abhyankar--Moh rectification,
Bhatwadekar--Dutta's relative kernel theorem and the standard
normalization/branch correspondence. It does not claim those
inputs, the Hamiltonian construction or branch multiplicity facts
as new. The statement concerns this exact fixed surface.

## Sources

[^am]: E. R. García Barroso and A. Płoski, [*An approach to plane algebroid branches*](https://arxiv.org/pdf/1208.0913), arXiv:1208.0913v1. The standing algebraically closed field convention, Section 1.2 on branches and formal order, Theorem 6.6 and its proof, and Theorem 6.9 with its proof were read directly. In characteristic zero its degree-divisibility conclusion yields rectification by the explicit decreasing-degree shears described above. It credits S. S. Abhyankar and T. T. Moh, [*Embeddings of the line in the plane*](https://doi.org/10.1515/crll.1975.276.148), *Journal für die reine und angewandte Mathematik* 276 (1975), 148–166. The original publisher full text was not accessible in this pass; the cited primary reconstruction was used.

[^bd]: S. M. Bhatwadekar and A. K. Dutta, [*Kernel of Locally Nilpotent R-Derivations of R[X,Y]*](https://repository.ias.ac.in/3203/1/311.pdf), *Transactions of the AMS* 349(8) (1997), 3303–3319, Theorem 4.7. Its exact statement, irreducibility definition and standing base-ring assumptions were reread in this pass. The complete selected proof was read directly during the independent [pass-27 relative-completion audit](relative-completion-pass27.md); repeated fetches of the proof pages timed out in this pass. The introduction also credits the earlier UFD-base kernel theorem of Daigle and Freudenburg. Here both the regular-sequence and comaximal cases supply the kernel, and no slice is inferred from the regular-sequence case.

[^branches]: The Stacks Project, [Lemma 33.40.1, Tag 0C1S](https://stacks.math.columbia.edu/tag/0C1S), normalization fibers and the number of branches. The statement and proof were read directly. For the fixed surface's actual finite normalization, gluing and double-normal-crossing local rings, see [pass 20](nodal-conductor-pass20.md), [pass 23](nodal-elimination-pass23.md) and [pass 24](nodal-hypersurface-pass24.md).
