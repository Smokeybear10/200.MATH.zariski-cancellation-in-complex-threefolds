# What the time-degree theorem controls

The published exponential-minimal-polynomial theorem applies to the
actual four-coordinate time-degree-two action. Its conclusion is a
finite-difference identity for the coordinate map, not an affine
generic slice or a bound in the separate intrinsic degree.

The exact degree-module theorems likewise do not identify the
generic-affine module used in the current slice-selection problem.
The faithful pass57 control makes that distinction concrete. This
is a bounded applicability result, not a claim that no relevant
theorem exists or that the full actual-coordinate implication is
false.

## 1. The actual time-degree theorem

Let \(E\) be an LND of \(\mathbb C[x_1,\ldots,x_4]\), and assume
\[
E^3x_i=0\quad(1\le i\le4),\qquad E^2x\ne0.
\tag{1}
\]
Zygadło's main theorem identifies the minimal polynomial of the
polynomial map \(F=\exp(E)x\) with \((T-1)^d\), where
\(d=\min\{m:E^m x_i=0\text{ for all }i\}\). Thus here
\[
F^{\circ3}-3F^{\circ2}+3F-\operatorname{Id}=0,\qquad
F^{-1}=3\operatorname{Id}-3F+F^{\circ2}.
\tag{2}
\]
These are coordinate-map identities, not
\((F^*-\operatorname{Id})^3=0\) on the entire algebra.
The proof uses finite differences of \(\exp(jE)x_i\), not
Jacobian invertibility or a slice condition.[^time]
Its calculation also holds componentwise on any finite list
satisfying (1), including the non-coordinate generators in
pass57. It provides no bound for the module \(V\) below.

## 2. Three filtrations must not be exchanged

In the supplied full-frame branch, retain
\[
B=A[s_*],\quad Es_*=1,\qquad C=\ker D,\quad
R=C_{\mathfrak m},\quad L=\operatorname{Frac}R,
\]
\[
\mathcal B=B_R,\quad \mathcal A=A_R,\qquad
\mathcal B_L=L[x_3,x_4],\qquad
E=f\partial_{x_3}+g\partial_{x_4}.
\tag{3}
\]
Here \(D\) is the distinct primitive intrinsic LND of \(A\).
The objects relevant to a proposed bound are
\[
F_n(E)=\ker(E^{n+1}:\mathcal B\to\mathcal B),\qquad
F_n(D)=\ker(D^{n+1}:\mathcal A\to\mathcal A),
\]
\[
V=\mathcal B\cap L[x_3,x_4]_{\le1}.
\tag{4}
\]
The last subscript means total degree in the generic bad pair.
The slice theorem gives
\[
F_n(E)=\bigoplus_{i=0}^n\mathcal A s_*^i,\qquad
E^nF_n(E)=\mathcal A\quad(n\ge1).
\tag{5}
\]
The image-ideal equivalence for a sliced derivation is explicitly
stated and proved in Dasgupta–Lahiri, Lemma 2.9.[^images]

By contrast, the exact affine-slice condition is
\[
\mathfrak a_{\mathrm{aff}}=E(V)\subseteq R,\qquad
\mathfrak a_{\mathrm{aff}}=R
\ \Longleftrightarrow\
\text{some actual }v\in V\text{ satisfies }Ev=1.
\tag{6}
\]
The finite freeness of \(V\), its basis containing \(1\), and (6)
are proved in [the pass57 module note](affine-slice-module-pass57.md).
Equation (5) does not identify \(V\) with \(F_1(E)\), or with a
degree module for \(D\). In particular, the slice already makes
every image ideal for \(E\) the unit ideal before (6) is known.

Freudenburg's Theorem 4.4 calculates a fixed degree module for
one LND by successive saturation using an actual local slice.
Under a Noetherian kernel the ascending chain stabilizes. The
proof and its Lemmas 4.1 and 4.3 were read directly: it uses
finite generation of that fixed module, not a uniform bound on
the stabilization index. Its input and output use the same
derivation throughout.[^modules]
This algorithm was already audited in
[pass21](universal-bridge-pass21.md). It is not a new route from
the \(E\)-degree bound (1) to the different module \(V\).

## 3. The faithful control separates these conclusions

The complete
[faithful pass57 construction](faithful-quadratic-slice-boundary-pass57.md)
has
\[
R=\mathbb C[a,v]_{(a,v-1)},\qquad
\mathcal A=R[t,z]/(t^2-v-az),\qquad
\mathcal B=\mathcal A[s],\quad E=\partial_s.
\tag{7}
\]
It is a smooth faithfully flat invariant localization of a
polynomial cylinder. Set
\[
w=as+tz,\quad q=ts+z^2,\quad
X=w,\quad Y=vw+t,\quad Q_1=z+w^2,\quad Q_2=q+w^2.
\tag{8}
\]
These four elements generate \(\mathcal B\) over \(R\), have
quadratic generic expressions, and are killed by \(E^3\).
The exact equalities established there are
\[
V=R\cdot1\oplus Rt\oplus Rw,\qquad E(V)=aR,
\]
\[
\min_{E\sigma=1}
\deg_t\bigl(\sigma-w/a\bigr)=3.
\tag{9}
\]
Equations (5), including all unit \(E\)-image ideals and their
free degree modules, still hold in this same example.
So freeness and principality statements about \(E\) cannot
alone turn the proper ideal in (9) into \(R\).

For clarity, the minimum in (9) concerns every actual slice.
The monic decomposition \(\mathcal A=R[z]\oplus tR[z]\)
forces the odd part of a hypothetical degree-at-most-two
correction to contain the impossible coefficient \(-1/a\)
of \(tz\). This is not merely the large degree of one chosen
slice. The full argument and the projection-degree conclusion
remain in the cited note.

The selected list in (8) has Jacobian rank three at
\((a,t,z,s)=(0,1,0,0)\), rather than four. It is therefore
not an actual ambient coordinate system, even locally there.
The full adjoint hypotheses are not realized. Accordingly,
this control does not disprove a theorem using precisely
that missing coordinate condition. It does show that any such
theorem must use more than the generic quadratic expressions,
time-degree identities, faithful flatness, and (5).

## 4. Exact remaining source gate

An applicable positive statement must use the actual polynomial
coordinate system, or its full adjoint identities, to prove
\(E(V)=R\), a weaker finite gauge bound, or recognition by another
method. The finite-difference theorem does not make that step.
Neither does replacing \(E\)'s unit image ideals by the unrelated
intrinsic \(D\)-image ideals without a proven transfer.

The present source search located no theorem establishing this
specific transfer. Searches for slice degree, degree bounds,
quadratic exponential automorphisms, and degree modules were
checked against primary statements. The nearby proper-action
and relative-polynomial-plane results are already covered in
passes 55 and 56 and are not re-listed here.

No exact published antecedent of the selected pass57
all-slices minimum was identified in these bounded checks.
Its underlying triangular action and quadratic invariant are
classical and were already credited as such. This does not
establish novelty of its particular generator selection.

The degree-module algorithm and the elementary sliced-image
identity are inherited tools, now compared with (6).
No new symbolic suite, full regression, theorem of universal
slice selection, or cancellation conclusion is claimed.

## Sources and access

[^time]: Jakub Zygadło, *Minimal polynomial of an exponential
automorphism of \(\mathbb C^n\)*, author preprint
[arXiv:0801.0616v1](https://arxiv.org/pdf/0801.0616v1),
4 January 2008. The whole preprint was read. The university
[publication record](https://apacz.matinf.uj.edu.pl/publikacje/6728-minimal_polynomial_of_an_exponential_automorphism_of_cn)
identifies *Proceedings of the American Mathematical Society*
137 (2009), 1849–1853. Publisher access failed; no final-journal
proof comparison is claimed.

[^images]: Nikhilesh Dasgupta and Animesh Lahiri,
[*On image ideals of nice and quasi-nice derivations on R[X1,X2]*](https://arxiv.org/pdf/2302.13787v6),
arXiv:2302.13787v6, 24 July 2026, Lemma 2.9 and its full proof.
Only the positive-index sliced-image equivalence is used here,
not a relative-plane classification or a claim about the
generic affine-slice ideal.

[^modules]: Gene Freudenburg,
[*Canonical factorization of the quotient morphism for an affine Ga-variety*](https://arxiv.org/pdf/1602.08786v3),
Section 4, Lemmas 4.1 and 4.3 and Theorem 4.4 with proofs.
The actual degree-resolution algorithm and its applicability
were already recorded in the pass21 proof and source audit.
