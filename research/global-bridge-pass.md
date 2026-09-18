# Global bridge pass: what would turn a slice on affine four-space into cancellation

**Date:** 2026-09-12
**Status:** bounded proof-and-primary-source pass; the cancellation problem remains open

## 1. Outcome

**Later strengthening:** [intrinsic-quotient-surface-pass.md](intrinsic-quotient-surface-pass.md)
uses Kaliman--Saveliev to show that every intrinsic nonzero LND has
affine-plane quotient and that a free intrinsic action suffices for
cancellation. Thus a hypothetical exotic kernel must have fixed
points for every intrinsic action, a stronger restriction than the
nonproperness condition retained in this earlier note.

Let

\[
B=\mathbb C[x_1,x_2,x_3,x_4],\qquad E\in\operatorname{LND}(B),
\qquad E(s)=1,
\]

and put \(K=\ker E\). The slice theorem gives

\[
B=K[s].
\]

Thus \(K\) is a finitely generated smooth factorial three-dimensional
\(\mathbb C\)-domain, \(K^{*}=\mathbb C^{*}\), and \(K[s]\cong\mathbb C^{[4]}\).
Proving \(K\cong\mathbb C^{[3]}\) is exactly the characteristic-zero
three-dimensional cancellation problem, not a consequence of the slice
terminology.[^mlvsy]

The one-variable rigidity theorem gives an intrinsic bridge omitted in the
first version of this note: \(K\) cannot be rigid. Indeed, if it were rigid,
then \(\operatorname{ML}(K[s])=K\), whereas
\(K[s]\cong\mathbb C^{[4]}\) has Makar--Limanov invariant \(\mathbb C\).
Thus some nonzero \(d\in\operatorname{LND}(K)\) exists, and extending it by
\(d(s)=0\) produces an LND commuting with \(E\).[^cml-rigid]

This theorem does **not** produce an invariant ambient coordinate or an
independent commuting **coordinate** derivative. A useful closure criterion
is:

> If an independent coordinate LND \(T\) commutes with \(E\), and the induced
> LND \(d=T|_K\) acts properly on \(\operatorname{Spec}K\), then
> \(K\cong\mathbb A^3\).

The conclusion follows directly from Gurjar--Masuda--Miyanishi, Theorem
4.1.1: a stably affine threefold with a proper \(G_a\)-action is affine
three-space.[^gmm] In fact, this applies to any proper intrinsic action
supplied above, whether or not it came from a coordinate derivative. The
exact residual case has nonzero but nonproper, slice-free LNDs on \(K\).
Section 3 describes the additional constraints when a commuting coordinate
LND is available.

This is a reduction and obstruction map, not a solution.

## 2. Properness of the original slice action is already automatic

The action of \(E=\partial_s\) on
\(\operatorname{Spec}K\times\mathbb A^1_s\) is a globally trivial
\(G_a\)-torsor. Its action graph is a closed immersion: its image in
\((\operatorname{Spec}K\times\mathbb A^1)^2\) is the closed locus on which
the two \(K\)-coordinates agree, and the group parameter is the difference
of the two \(s\)-coordinates. Hence the \(E\)-action is proper.

Consequently, none of the following alone can be the missing theorem:

- the action has no fixed points;
- the action is proper;
- the invariant ring is affine;
- the quotient morphism is a globally trivial \(\mathbb A^1\)-bundle; or
- the quotient is smooth, factorial, and stably affine.

Every putative cancellation counterexample obtained from \(K[s]\cong
\mathbb C^{[4]}\) already has all of these properties.

The available positive proper-action theorems add a real hypothesis.
Kaliman proves that a proper \(G_a\)-action on \(\mathbb C^4\) which
preserves an ambient coordinate is a translation.[^kaliman] Dubouloz,
Finston, and Jaradat prove this for proper triangulable actions over a
characteristic-zero field.[^dfj] Neither theorem proves that an arbitrary
slice action preserves a coordinate or is triangulable.

The algebraic invariant-coordinate result is even more direct.
Bhatwadekar--Gupta--Lokhande, Theorem 3.5, says that if a nonzero
\(k[T]\)-linear LND of \(k[T,X,Y,Z]\) has regular kernel, then its kernel is
\(k[T]^{[2]}\).[^bgl] The slice already makes \(K\) regular. Thus one
ambient coordinate in \(K\) closes cancellation, but finding that coordinate
is exactly the unproved step.

Masuda's recent faithfully-flat criteria do not erase this boundary.
Theorems 3.5--3.6 give a fiber criterion for a quotient to be a trivial
\(\mathbb A^1\)-bundle; a slice has already supplied that conclusion.
Theorem 4.3 obtains an affine-three-space quotient only after assuming,
among other conditions, an invariant \(\mathbb A^3\)-fibration over
\(\mathbb A^1\) and factoriality of every induced quotient fiber.[^masuda]
For \(B=\mathbb C^{[4]}\), the needed invariant \(\mathbb A^3\)-fibration
amounts to the same kind of ambient-coordinate input used above.

As a useful warning outside affine four-space, Masuda's Example 4.2 starts
with a Koras--Russell threefold \(X_0\) and puts a slice action on
\(X_0\times\mathbb A^1\); its quotient is \(X_0\), not \(\mathbb A^3\).
This is not a cancellation counterexample because
\(X_0\times\mathbb A^1\) is not proved to be \(\mathbb A^4\). It does show
that smoothness, acyclicity, affineness of the quotient, and a global slice
do not identify the quotient without using the special ambient
\(\mathbb A^4\) hypothesis in a substantive way.

## 3. Exact centralizer reduction

Write \(B=K[s]\) and \(E=\partial_s\). Every derivation \(T\) commuting
with \(E\) has the unique form

\[
T=d+q\partial_s,\qquad d\in\operatorname{Der}_{\mathbb C}(K),\quad q\in K.
\tag{1}
\]

Indeed, commutation with \(\partial_s\) makes all coefficients independent
of \(s\). Moreover, \(T\) is locally nilpotent exactly when \(d\) is locally
nilpotent: necessity follows by restriction to \(K\), and sufficiency follows
because \(d\) is locally nilpotent on finite generators of \(K\) and
\(T^{n+1}(s)=d^n(q)\).

Suppose now that \(T\) is a coordinate LND, so it has a slice and

\[
R:=\ker T\cong\mathbb C^{[3]}.
\]

If \(d=0\), then \(T=q\partial_s\). A \(T\)-slice makes \(q\) a unit of
\(K\), hence \(q\in\mathbb C^*\), and \(K=\ker T\cong\mathbb C^{[3]}\).
Therefore every unresolved independent case has \(d\ne0\).

There is a second elementary closure.

**Constant-class lemma.** If

\[
q+d(h)=c\qquad\text{for some }h\in K,\ c\in\mathbb C,
\tag{2}
\]

then \(K\cong\mathbb C^{[3]}\).

If \(c\ne0\), replace \(s\) by \(s'=s+h\). Then
\(T=d+c\partial_{s'}\), and

\[
\theta(k)=\exp(-s'd/c)(k),\qquad \theta(s')=s'
\]

is a polynomial automorphism of \(K[s']\). Direct differentiation gives
\(T\theta(k)=0\), so \(\theta(K)=\ker T=R\), whence \(K\cong R\).
If \(c=0\), then \(s'\) is \(T\)-invariant. Expanding a \(T\)-slice in
powers of \(s'\) shows that its constant coefficient is a slice for \(d\).
Also, commutation makes \(E\) restrict to an LND on
\(R=\ker T\cong\mathbb C^{[3]}\), and \(E(s')=1\). Hence
\(R=K^d[s']\), and cancellation in dimension two gives
\(K^d\cong\mathbb C^{[2]}\). Consequently

\[
K=K^d[u].
\]

Thus again \(K\cong\mathbb C^{[3]}\).

Accordingly, a nonpolynomial residual case must satisfy

\[
d\ne0,\qquad d\text{ is nonproper and has no slice},\qquad
q\notin\mathbb C+d(K).
\tag{3}
\]

The properness assertion in (3) uses Gurjar--Masuda--Miyanishi; the other
two assertions follow from the preceding elementary argument.

The hypothesis that \(T\) is proper on \(B\) does not descend to properness
of \(d\) on \(K\). A minimal counterexample is

\[
B=\mathbb C[x,y,z,s],\qquad E=\partial_s,\qquad
T=\partial_s+x\partial_y.
\]

Both \(E\) and \(T\) have the slice \(s\), commute, and are coordinate
translations. But

\[
K=\ker E=\mathbb C[x,y,z],\qquad d=x\partial_y
\]

has fixed points and is not proper. It has no slice because
\(d(K)\subset xK\). This also disproves the tempting assertion that two
commuting coordinate LNDs with slices automatically yield a dual system of
slices.

**Correction from the global continuation:** \(K\) cannot be rigid. The
one-variable rigidity theorem gives \(\operatorname{ML}(K[s])=K\) for
rigid \(K\), contradicting \(\operatorname{ML}(\mathbb C^{[4]})=\mathbb C\).
See [the intrinsic-actions proof and primary sources](intrinsic-actions-pass.md).
Thus \(K\) has a nonzero LND; extending it to kill \(s\) supplies an LND
commuting with \(E\). What remains unproved is that this extension can be
chosen as a **coordinate** LND with a slice. The earlier assertion that
intrinsic nonrigidity was not known was incorrect. The stronger reduction to
a commuting coordinate partial is still an unproved structural assertion.

## 4. The vertical rank-three pair and its fibers

Now assume the additional presentation

\[
B=R[w],\qquad R=\mathbb C[x,y,z],\qquad
E=\delta+a\partial_w,\qquad T=\partial_w,
\]

where \(\delta\) has rank three. If \(E(s)=1\), then (1) applies and

\[
K^d=K\cap R=\ker\delta\cong\mathbb C^{[2]}.
\tag{4}
\]

For every prime \(\mathfrak p\) of \(A:=\ker\delta=K^d\), there is an exact
fiberwise stable isomorphism

\[
(K/\mathfrak pK)[s]\cong B/\mathfrak pB
\cong (R/\mathfrak pR)[w].
\tag{5}
\]

Over \(F=\operatorname{Frac}A\), a local slice for \(\delta\) gives
\(R_F\cong F^{[1]}\). Hence (5), together with cancellation for affine
curves, gives \(K_F\cong F^{[1]}\). The morphism
\(\operatorname{Spec}K\to\operatorname{Spec}A\cong\mathbb A^2\) is therefore
generically an affine-line fibration.

This does not control its bad fibers. If it were faithfully flat and every
closed fiber were \(\mathbb A^1\), the standard affine-line-bundle criterion
would make it an \(\mathbb A^1\)-bundle; over affine plane the corresponding
line bundle and additive torsor are trivial, yielding \(K=A^{[1]}\).
But the same argument applied to \(R\) would make
\(R=A^{[1]}\) and force \(\delta\) to have rank one. Thus a rank-three
\(\delta\) necessarily puts the obstruction on special fibers. Any proof
which silently replaces the generic \(F^{[1]}\) calculation by an all-fiber
statement has already discarded the only possible residual case.

For LNDs on \(\mathbb C^{[3]}\), the required flatness itself is available:
Dasgupta--Gaifullin, Theorem 2.10(i), records the Bonnet--Daigle--Kaliman
plinth theorem that \(\mathbb C^{[3]}\) is faithfully flat over the kernel
of any LND.[^dg] Flatness does not make a reducible or nonreduced bad fiber
an affine line.

Finally, a principal \(G_a^2\)-torsor argument cannot apply to the
rank-three pair. A dual slice system for \((E,T)\) would require an element
\(u\in R\) with \(\delta u=1\), as well as an invariant companion to \(w\).
The first condition would make \(\delta\) rank one. Thus the two individual
proper slice actions need not combine into a proper free \(G_a^2\)-action.

## 5. A concrete obstruction to an overbroad gauge theorem

The Danielewski surfaces give an exact model showing that commutation, an
irreducible base LND, reduced plinth, and even an affine-in-\(w\) slice do
not force a constant-plus-derivative coefficient over an arbitrary smooth
base.

Let

\[
S_1=\operatorname{Spec}
\frac{\mathbb C[x,y,z]}{(xy-z^2+1)},\qquad
\delta x=0,\quad\delta z=x,\quad\delta y=2z,
\]

and extend \(\delta\) to \(S_1\times\mathbb A^1_w\) by

\[
\mathcal E=\delta+\frac{3y}{2}\partial_w.
\]

Then

\[
s=\frac{zy}{2}-xw
\]

satisfies \(\mathcal E(s)=1\). Define

\[
\begin{aligned}
Z&=x^2w+\frac{3z-z^3}{2},\\
Y&=x^2w^2+(3z-z^3)w+\frac{y^2(z^2-4)}4.
\end{aligned}
\]

Direct calculation gives

\[
\mathcal E(x)=\mathcal E(Z)=\mathcal E(Y)=0,\qquad
x^2Y=Z^2-1.
\]

The inverse polynomial formulas are

\[
\begin{aligned}
z&=Z+xs,\\
y&=xY+2Zs+xs^2,\\
w&=\frac{ZY}{2}+\frac{3xYs}{2}
  +\frac{3Zs^2}{2}+\frac{xs^3}{2}.
\end{aligned}
\]

Thus

\[
\mathcal O(S_1)[w]\cong
\frac{\mathbb C[x,Y,Z]}{(x^2Y-Z^2+1)}[s],
\qquad
\ker\mathcal E\cong\mathcal O(S_2).
\]

The surfaces \(S_1\) and \(S_2\) are nonisomorphic, while their cylinders
are isomorphic. Moser-Jauslin--Poloni describe the primary geometric
mechanism: every \(S_n:x^ny=z^2-1\) is a principal \(G_a\)-bundle over the
affine line with doubled origin, and the fiber product of two such bundles
is a trivial bundle over either affine surface.[^mjp]

If \(3y/2=c+\delta H\) with \(c\in\mathbb C^*\), the standard
shear-and-flow straightening would identify
\(\ker\mathcal E\) with \(\mathcal O(S_1)\), contradicting
\(S_1\not\cong S_2\). Hence this is a genuine nongauge slice. For
\(\delta\) on \(S_1\), the plinth ideal is \((x)\subset\mathbb C[x]\),
which is radical, and \(\delta\) is irreducible.

This example is not a counterexample to affine-three-space cancellation:
\(\mathcal O(S_1)\) is not a polynomial three-variable base (indeed it is
only two-dimensional), and its cylinder is not being identified with
\(\mathbb A^3\). It precisely blocks attempts to prove the gauge conclusion
from commutation and reduced plinth alone.

## 6. A complete affine-in-\(w\) bridge for the fixed Freudenburg derivation

For the project's fixed derivation

\[
\Delta=\operatorname{Jac}(f,g,\cdot),\qquad
\Delta r=fg,\qquad \ker\Delta=\mathbb C[f,g],
\]

the known special fibers repair the failure seen in Section 5.
Suppose

\[
E=\Delta+a\partial_w,\qquad
s=u(f,g)w+v,\qquad E(s)=1.
\]

Then

\[
\Delta v+ua=1. \tag{6}
\]

Dasgupta--Gaifullin's faithful-flatness theorem justifies the following
argument even when an irreducible zero curve of \(u\) is singular. For an
irreducible factor \(p\) of \(u\), pass to a normalization DVR \(V\) at a
point where \(p=0\) meets one of the axes \(fg=0\). Factorial closedness of
\(\mathbb C[f,g]\) in \(R\), together with the UFD property of \(R\), makes
\(pR\) prime. Faithful flatness makes

\[
(R/pR)\otimes_{\mathbb C[f,g]/p}V
\]

a nonzero \(V\)-flat domain inside its generic fiber. Away from \(fg=0\)
that generic fiber is \(\operatorname{Frac}(V)[r]\).

Equation (6) descends to a slice. Its kernel \(H\) satisfies

\[
V\subseteq H\subseteq\operatorname{Frac}(V).
\]

If \(H\) contained an element of negative valuation, a uniformizer would
become invertible and the special fiber would be empty. Faithful flatness
excludes that, so \(H=V\); the special fiber would have to be one affine
line. This contradicts the actual two-line fibers over
\((f,g)=(c,0)\), the five-line fibers over \((0,d)\), and the nonreduced
fiber at the origin. Therefore \(u\) has no zero on either coordinate axis,
and

\[
u=c+fgQ,\qquad c\in\mathbb C^*.
\]

In the \(\mathbb C[f,g]\)-module \(R/\Delta R\), every element is killed by
a power of \(fg\), because localization at \(fg\) gives the slice
\(r/(fg)\). Multiplication by \(c+fgQ\) is therefore invertible on each
element by a finite geometric series. Reducing (6) modulo \(\Delta R\)
then yields

\[
a=c^{-1}+\Delta H
\]

for some \(H\in R\). Thus every affine-in-\(w\) slice in this fixed family
is gauge and has polynomial kernel.

This affine argument was the last degree-bounded gap when it was written.
The subsequent all-degree orbit argument summarized in Section 8 supersedes
that gap for this fixed \(\Delta\): it does not reduce a general slice to an
affine one, but excludes every nongauge coefficient directly.

## 7. First quadratic identity, and why axis-square residues do not finish it

Let

\[
s=b_2w^2+b_1w+b_0,\qquad E(s)=1.
\]

Coefficient comparison gives

\[
\Delta b_2=0,\qquad
\Delta b_1+2ab_2=0,\qquad
\Delta b_0+ab_1=1.
\tag{7}
\]

Eliminating \(a\) gives the exact identity

\[
\Delta(4b_2b_0-b_1^2)=4b_2.
\tag{8}
\]

The proved plinth equality
\(\Delta R\cap\mathbb C[f,g]=fg\,\mathbb C[f,g]\) therefore forces

\[
b_2=fgP(f,g).
\]

Using \(\Delta r=fg\), equation (8) becomes

\[
b_1^2-4fgP\,b_0=-4rP+Q(f,g)
\tag{9}
\]

after renaming an invariant \(Q\). This is a genuine narrowing: every
quadratic slice has leading coefficient supported on the bad-axis divisor.

Without the normalization forced by the fixed line, square residues on the
two axes alone do not force \(P=0\).
Modulo \(f\), one has \(r=-x^3\), \(g=x^5\), and the induced kernel is
\(\mathbb C[x]\). Equation (9) permits identities of the form

\[
B(x)^2=4x^3P(0,x^5)+Q(0,x^5);
\]

for example \(B=x^4\), \(P(0,G)=G/4\), \(Q(0,G)=0\) satisfies this boundary
identity. This example is **not** admissible boundary data for an actual
slice: on the fixed line \(x=y=0\), the slice equation forces
\(b_1(0)=1/c\ne0\), whereas \(B(0)=0\). Modulo \(g\), the induced invariant
ring contains
\(\mathbb C[f,r]/(r^2+f^3)\), and

\[
(A(f)+rB(f))^2
=A(f)^2-f^3B(f)^2+2rA(f)B(f),
\]

which realizes many nonzero \(rP(f,0)\) terms before all slice conditions are
imposed. These examples show only that equation (9), stripped of the
fixed-line normalization and the two remaining equations in (7), is too weak.
They do **not** refute the stronger sparse-square statement with
\(b_1(0)=1/c\ne0\); that isolated lemma remains unproved. It is no longer
needed for the fixed-\(\Delta\) classification, because the all-degree orbit
proof does not proceed by eliminating \(P\).

## 8. All-degree fixed-\(\Delta\) result and hostile audit

The later proof appendix establishes the following working theorem for the
specific Freudenburg derivation over a characteristic-zero field:

\[
\Delta+a\partial_w\text{ has a polynomial slice}
\quad\Longleftrightarrow\quad
a=c+\Delta H,
\qquad c\in k^*,\ H\in k[x,y,z]. \tag{10}
\]

The forward direction first reduces any putative slice to
\(a=c+\Delta H/f^m\). For a minimal nonremovable \(m\ge2\), low homogeneous
parts of \(H\) can be subtracted as invariants, leaving every contributing
degree \(D>2m-4\). On the two exact branches

\[
x_0=B\phi(F^3/B^6),\qquad
x_1=\zeta B\phi(\zeta^{-1}F^3/B^6),
\qquad \phi^6-\phi+U=0,\quad \phi(0)=1,
\]

the collected endpoint difference has terms \(B^LF^J\) with
\(L+2J=D\). Choosing the least Newton slope
\((L+2)/(m-1-J)>2\) produces a leading polynomial in a unit \(V\) with a
nonzero top term and a nonzero lower term. Formal Weierstrass preparation
lifts a nonzero root even when it is multiple. The resulting two integral
endpoints have zero \(w\)-displacement but orbit time of valuation
\(-M-2N<0\), contradicting any polynomial slice.

The hostile reconstruction specifically checked four possible failure points:

1. fifth-divisible raw exponents were not discarded; all corrections from
   the formal branch were collected with the factor \(\zeta^L-1\);
2. the degree identity \(L+2J=D\) survives every correction, and terms with
   \(J\ge m-1\) are strictly above the selected edge;
3. a fixed \(J\) determines \(L\) on the edge, so the asserted lower term
   cannot disappear through uncollected same-power cancellation; and
4. Weierstrass preparation, rather than simple-root Hensel lifting, handles
   a multiple leading root while preserving that \(V\) is a unit.

No algebraic gap was found in this bounded reconstruction. This upgrades the
old affine-family gap to a **complete working proof for all vertical
coefficients of this one fixed base**, with independent model audit and exact
finite controls. It is not human certification, an originality result, or a
step that represents an arbitrary slice LND on \(\mathbb A^4\) in this form.
The full derivation is in
[arbitrary-coefficients-pass.md](arbitrary-coefficients-pass.md), Sections
5 and 8.

The same orbit proof, together with the positive gauge normal form, yields
the sharper fixed-family geometric classification

\[
E_a\text{ is proper}\quad\Longleftrightarrow\quad
E_a\text{ has a slice}\quad\Longleftrightarrow\quad
a=c+\Delta H\quad(c\ne0).
\]

This remains a theorem about one vertical family. It supplies no global
normal-form bridge for arbitrary slice LNDs on affine four-space.

## 9. Claim boundary and remaining global proof obligation

What is proved in this note:

1. the exact centralizer form (1);
2. the constant-class closure (2);
3. the residual conditions (3), using the cited proper-action theorem;
4. the fiberwise stable relation (5);
5. the explicit Danielewski nongauge counterexample;
6. the fixed-\(\Delta\) affine-slice bridge;
7. the quadratic identities (7)--(9), with the fixed-line caveat above; and
8. the independently reconstructed working proof of (10) for every
   \(a\in k[x,y,z]\).

What is not proved:

- existence of an independent commuting coordinate LND for every slice LND
  on \(\mathbb C^{[4]}\);
- properness of the induced \(d\);
- an invariant ambient coordinate;
- representation of an arbitrary slice LND on \(\mathbb C^{[4]}\) as a
  vertical extension of this fixed \(\Delta\); or
- cancellation in dimension three over \(\mathbb C\).

The former quadratic target is therefore retired as a route to the fixed-base
classification. The real global target remains a structural bridge from an
arbitrary slice LND to an invariant ambient coordinate or to a controlled
vertical normal form. Testing only (9) on \(f=0\) and \(g=0\) cannot supply
that bridge.

## 10. Targeted post-proof collision screen

The exact statement screened was (10), including arbitrary
\(a\in k[x,y,z]\), the slice criterion, and the constant-plus-image
conclusion. The closest primary statements found have materially different
hypotheses or conclusions:

- Freudenburg's original paper constructs the homogeneous rank-three base
  derivation and embeds maximal-rank actions in higher affine dimensions; its
  publisher statement does not give a slice criterion for arbitrary vertical
  coefficients.[^freudenburg-original] Kaliman's full-text survey reproduces
  the exact \(F,G,R\) example and uses it to illustrate homogeneous rank-three
  actions, not extensions with \(E(w)=a\).[^kaliman-survey]
- Sun--Liu prove that the image of every rank-three homogeneous LND on
  \(k^{[3]}\) is a Mathieu--Zhao subspace, using local-slice constructions.
  That is a property of \(\operatorname{im}\Delta\); it neither decides
  membership \(a-c\in\Delta R\) for this \(\Delta\) nor classifies slices of
  \(\Delta+a\partial_w\).[^sun-liu]
- Freudenburg's later extension machinery starts with an invariant coefficient
  \(a\in\ker D\); Proposition 7.1 also assumes
  \(aA\cap I_n=aI_n\), and Theorem 7.6 assumes a fundamental pair and
  \(a\in A_0\). It computes kernels and, in that setting, characterizes
  surjectivity of the quotient. It does not cover an arbitrary coefficient
  in \(R\) or assert (10).[^freudenburg-extension]
- Dasgupta--Gaifullin reproduce the fixed \(\Delta\), extend it to a larger
  family of rank-three derivations on \(k^{[3]}\), and characterize LNDs on
  the base which commute with an irreducible rank-three LND. Their theorem is
  on \(R\), not a slice classification on \(R[w]\).[^dg]
- Proper-action results close a positive case only after an invariant ambient
  coordinate or triangulability is known; those hypotheses are not a
  coefficient test for this family.[^kaliman][^dfj]

Exact-expression searches included “xz-y²” with
“zf²+2x²yf+x⁵”, “r²+f³=xg”, “c+D(H)” with
“locally nilpotent derivation”, “vertical extension LND slice”,
“Freudenburg derivation proper extension”, and the forward-citation list of
the 1998 construction. In this bounded screen, no inspected statement
matched (10). That is not evidence of absence: thesis/full-database and
specialist review remain outstanding, so the result stays **internally
proved / originality unresolved**.

## Primary sources and access

All theorem statements used above were checked in full primary text. The
original 1998 Freudenburg item in Section 10 was accessible only through its
publisher record and abstract and is used only to delimit that screen, not as
theorem evidence.

[^mlvsy]: Leonid Makar-Limanov, Peter van Rossum, Vladimir Shpilrain, and Jie-Tai Yu, [“The Stable Equivalence and Cancellation Problems,” Section 3, printed pp. 347--348](https://ems.press/content/serial-article-files/43009), *Commentarii Mathematici Helvetici* 79 (2004), 341--349, DOI 10.1007/s00014-003-0796-3. The paper explicitly records the slice-kernel formulation as equivalent to cancellation.
[^cml-rigid]: Anthony J. Crachiola and Leonid G. Makar-Limanov, [“An Algebraic Proof of a Cancellation Theorem for Surfaces,” Theorem 3.1](https://doi.org/10.1016/j.jalgebra.2008.03.037), *Journal of Algebra* 320 (2008), 3113--3119; [accessible manuscript](https://cds.cern.ch/record/905059/files/cer-002575268.pdf). For a finitely generated rigid domain \(A\), it gives \(\operatorname{ML}(A[t])=A\).
[^gmm]: R. V. Gurjar, Kayo Masuda, and Masayoshi Miyanishi, [*Affine Space Fibrations*, Theorem 4.1.1, printed p. 44](https://oa.tib.eu/renate/bitstreams/2db0f47c-00f9-4195-9c8a-a46722165a99/download), Oberwolfach Preprint OWP-2018-19, DOI 10.14760/OWP-2018-19. It assumes a three-dimensional affine \(X\), \(X\times\mathbb A^{n-3}\cong\mathbb A^n\) for \(n\ge4\), and a proper \(G_a\)-action.
[^kaliman]: Shulim Kaliman, [“Proper \(G_a\)-Actions on \(\mathbb C^4\) Preserving a Coordinate,” Theorem 0.1 and Theorem 9.11](https://arxiv.org/pdf/1506.06082), *Algebra & Number Theory* 12 (2018), 227--266, DOI 10.2140/ant.2018.12.227.
[^dfj]: Adrien Dubouloz, David R. Finston, and Imad Jaradat, [“Proper Triangular \(G_a\)-Actions on \(\mathbb A^4\) Are Translations,” main corollary](https://arxiv.org/pdf/1303.1032), *Algebra & Number Theory* 8 (2014), 1959--1984, DOI 10.2140/ant.2014.8.1959.
[^bgl]: S. M. Bhatwadekar, Neena Gupta, and Swapnil A. Lokhande, [“Some K-Theoretic Properties of the Kernel of a Locally Nilpotent Derivation on \(k[X_1,\ldots,X_4]\),” Theorem 3.5, arXiv PDF p. 11](https://arxiv.org/pdf/1501.01438), *Transactions of the American Mathematical Society* 369 (2017), 341--363, DOI 10.1090/tran/6649.
[^masuda]: Kayo Masuda, [“Faithfully Flat Quotient Morphisms by \(G_a\)-Actions on Factorial Affine Varieties,” Theorems 3.5, 3.6, 4.3 and Example 4.2](https://arxiv.org/pdf/2512.06687), *Journal of Algebra* 691 (2026), 577--596, DOI 10.1016/j.jalgebra.2025.11.020.
[^dg]: Nikhilesh Dasgupta and Sergey A. Gaifullin, [“On Locally Nilpotent Derivations of Polynomial Algebra in Three Variables,” Theorems 2.10 and 4.5 and Section 5](https://arxiv.org/pdf/2306.00510), *Sbornik: Mathematics* 216 (2025), 456--484, DOI 10.4213/sm10094e.
[^mjp]: Lucy Moser-Jauslin and Pierre-Marie Poloni, [“Isomorphisms Between Cylinders over Danielewski Surfaces,” Introduction and Section 2.2](https://arxiv.org/pdf/2002.12202), *Beiträge zur Algebra und Geometrie* 62 (2021), no. 4, 755--771, DOI 10.1007/s13366-020-00548-x.
[^freudenburg-original]: Gene Freudenburg, [“Actions of \(G_a\) on \(A^3\) Defined by Homogeneous Derivations,” publisher record and abstract](https://www.sciencedirect.com/science/article/pii/S0022404996001430), *Journal of Pure and Applied Algebra* 126 (1998), 169--181, DOI 10.1016/S0022-4049(96)00143-0. The bounded audit had publisher abstract/metadata access, not searchable full text.
[^kaliman-survey]: Shulim Kaliman, [“Actions of \(\mathbb C^*\) and \(\mathbb C^+\) on Affine Algebraic Varieties,” Example 10.5(2) and Theorem 10.7](https://www.math.miami.edu/~kaliman/library/seattle.paper.pdf), in *Algebraic Geometry—Seattle 2005*, Proceedings of Symposia in Pure Mathematics 80 (2009), 629--654.
[^sun-liu]: Xiaosong Sun and Dayan Liu, [“Images of Locally Nilpotent Derivations of Polynomial Algebras in Three Variables,” Sections 4--5](https://www.sciencedirect.com/science/article/pii/S0021869320305512), *Journal of Algebra* 569 (2021), 401--415, DOI 10.1016/j.jalgebra.2020.10.025.
[^freudenburg-extension]: Gene Freudenburg, [“Actions of \(SL_2(k)\) on Affine \(k\)-Domains and Fundamental Pairs,” Proposition 7.1 and Theorem 7.6](https://arxiv.org/html/2108.12021), *Transformation Groups* 29 (2024), 959--1003.

Exact searches included: “proper \(G_a\) action affine four-space
translation,” “slice LND \(k[x_1,\ldots,x_4]\) kernel polynomial
cancellation,” “commuting locally nilpotent derivations \(A^4\) coordinate
partial,” “slice LND centralizer coordinate derivation,” “free \(G_a^2\)
action \(A^4\) quotient \(A^2\),” and the citation trails of
Kaliman, Dubouloz--Finston--Jaradat, Bhatwadekar--Gupta--Lokhande,
Gurjar--Masuda--Miyanishi, and Moser-Jauslin--Poloni. The one abstract-only
record is identified explicitly above and was not used as theorem evidence;
no AI-generated source was used.
