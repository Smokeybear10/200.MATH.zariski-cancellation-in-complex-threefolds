# Homogeneous-speed recognition: exact primary-source scope

The bounded primary-source comparison did not locate a theorem with the
exact pass89 hypotheses below. The checked quasi-nice results retain a
polynomial-base or ambient-coordinate premise. The closest directly usable
additional criterion is strong nilpotence of the actual Jacobian under
independent evaluations. It implies recognition, including in the
nonconical case, but is stronger than the available single-point nilpotence.
This is an applicability audit, not a claim of historical novelty or a
complete literature search.

## 1. Exact statement and terminology

The working [pass89 theorem](constant-acceleration-relative-slice-descent-pass89.md)
concerns actual coordinates and an actual complex locally nilpotent derivation:
\[
B=\mathbb C[x_1,x_2,x_3,z],\qquad E^2x_i=0\ (i\le3),\qquad
E^2z=q\in\mathbb C^*,\qquad
0\ne F\in\mathbb C[T_1,T_2,T_3]\text{ homogeneous},\quad
F(Ex_1,Ex_2,Ex_3)=0.
\tag{1}
\]
Its conclusion is \(A=\ker E\simeq\mathbb C^{[3]}\).
The slice \(u=Ez/q\) is automatic. Thus E is fixed-point-free and
irreducible, and \(A\simeq B/(u)\) is regular. None of these observations
assumes that u is an ambient polynomial coordinate.

Dasgupta--Lahiri Definitions 2.2--2.3 call the supplied frame
three-quasi-nice. Nonzero q does not prove *strict* three-quasi-niceness,
which excludes nicer frames after arbitrary polynomial coordinate changes.
Their current arXiv record remains v6, dated 24 July 2026.[^dl]

Homogeneity here concerns a relation among the three speeds. It does not
make E a homogeneous derivation or bound its ordinary coefficient degrees.
The rank of an LND in the cited literature counts missing invariant
ambient coordinates; it is not \(\operatorname{rank}J\), where
\(P=E(x_1,x_2,x_3,z)^t\) and \(J=\operatorname{Jac}P\).

## 2. The checked recognition statements need more than (1)

Dasgupta--Gupta Theorem 4.1 reproduces Wang's classification with two
time-linear coordinates on an actual polynomial three-ring over a field.
Their Theorem 4.8 reproduces Daigle's theorem starting with one nonzero
time-linear coordinate, also in three variables. Proposition 4.4 requires
an actual polynomial three-ring over a fixed PID and a specified generic
triangular case. Corollary 3.8 requires an invariant ambient coordinate
and full niceness of the remaining three coordinates.[^dg]

Bhatwadekar--Gupta--Lokhande Theorem 3.5 has a simpler sufficient gate
for the present problem: an actual invariant ambient coordinate and a
regular kernel imply a polynomial kernel. Its proof localizes the fixed
one-variable base at every maximal ideal, applies its DVR result, and
then its local-global polynomial-ring theorem.[^bgl] Regularity is already
available above; the ambient coordinate is not.

For example, if \(\partial_z(Ex_i)=0\) for all three good coordinates,
E restricts to a nice LND of the actual ring
\(\mathbb C[x_1,x_2,x_3]\). If nonzero, the exact Wang statement in
Dasgupta--Gupta Theorem 3.1(i) gives an invariant constant linear form.
If zero, any good coordinate is invariant. Bhatwadekar--Gupta--Lokhande
then applies. This is the established stable-good-ring subcase, not a new
consequence of (1).

Dasgupta--Lahiri Lemma 2.12 starts with an actual \(R[X,Y]\), with R a
fixed UFD. Its quasi-nice kernel description cannot be applied merely
because A has relative generators over an invariant plane. Theorem 5.2
also assumes a non-fixed-point-free action, unlike E here. For the
original E, its Lemma 2.9 already gives every full image ideal equal to A:
\[
A\cap E^j(B)=A\quad(j\ge1),\qquad
E^j\left(\frac{a u^j}{j!}\right)=a\quad(a\in A).
\tag{2}
\]
Consequently those image-ideal formulas do not decide the actual
inclusion of the smaller relative generator ring in A.

## 3. Quasi-translation and newer rank theorems do not remove the gate

De Bondt's quasi-translation criterion is exactly
\(\operatorname{Jac}(H)H=0\). In the present frame the identities are
instead
\[
\Phi_t(x)=x+tP(x)+\frac{qt^2}{2}e_4,\qquad
JP=qe_4\ne0,\qquad EJ=-J^2,\qquad J^4=0.
\tag{3}
\]
The first identity follows from the finite exponential. Differentiating
\(EP=qe_4\) gives the third; the flow Jacobian is \(I+tJ\), whose
determinant is one, giving the last. A nonlinear relation among three
entries of P is not a replacement for the missing quasi-translation
identity.[^qt]

Dasgupta--Gaifullin's newer rank and commuting-LND analysis was checked
in arXiv:2306.00510v2. Proposition 4.1 and its complete proof start on
\(k^{[3]}\); Theorem 4.5 has that same section-wide premise. Applying
them to a highest LND on the unknown A would assume the conclusion
\(A\simeq\mathbb C^{[3]}\). Their general-n Theorem 3.20 instead assumes
LND rank at most two, not a small polynomial Jacobian rank.[^dga]
Thus these statements do not upgrade the already known intrinsic
invariant plane to an ambient coordinate plane.

## 4. A source-backed criterion that also works when Omega is nonzero

De Bondt, Proposition 1.3 of arXiv:1601.00579v4, proves that a polynomial
matrix is strongly nilpotent over an infinite extension field exactly
when it is similar over its coefficient field to a strictly triangular
matrix. Strong nilpotence means products at arbitrarily and independently
chosen evaluation points vanish. In dimension four the following is
therefore a sufficient additional hypothesis:
\[
J(\xi^{(1)})J(\xi^{(2)})J(\xi^{(3)})J(\xi^{(4)})=0
\quad\text{for four independent four-tuples of indeterminates.}
\tag{4}
\]
It is also equivalent to strong nilpotence here, since a product of four
strictly triangular four-by-four matrices is zero. The selected proof
extracts a common constant kernel vector from a nonzero shortest product,
then inducts on the remaining block.[^strong]

After constant similarity, the first row of a lower triangular matrix
is zero. Thus there is a nonzero constant row \(\ell\) with
\(\ell J=0\), and \(\ell P=c\in\mathbb C\). The actual linear coordinate
\(L=\ell x\) satisfies \(EL=c\). If c is nonzero, L/c is an ambient
coordinate slice and evaluation at L=0 identifies A with a polynomial
three-ring. If c is zero, the invariant-coordinate theorem in Section 2
applies. This elementary application does not use F or Omega.

Equation (3) evaluates all factors at the same point. No implication
from (3) to the independent-evaluation identity (4) has been proved here.
The same de Bondt paper's Theorems 3.2--3.3 concern ordinary quadratic
coefficient maps, with respectively Jacobian rank at most two or square-zero
Jacobian. Neither their degree premise nor their rank premise is supplied
by the remaining rank-two-speed, rank-three-Jacobian case.[^strong]

A concrete actual boundary is obtained, for any nonconstant polynomial
\(f\in\mathbb C[t]\), from canonical coordinates \((u,r,t,c)\) and
\(E=\partial_u\):
\[
\begin{gathered}
x_1=u,\quad x_2=t+ur,\quad x_3=c+u f(t),\quad z=r+u^2,\\
r=z-x_1^2,\quad t=x_2-x_1r,\quad c=x_3-x_1f(t),\\
b=(1,r,f(t)),\qquad E^2z=2,\qquad
\det[b,b_r,b_t]=f'(t)\ne0.
\end{gathered}
\tag{5}
\]
The displayed inverse is polynomial. There is no nonzero homogeneous
relation among b: dehomogenization at the first entry 1 and algebraic
independence of r and f(t) prove this directly. Spatial degrees are
unbounded as f varies. These actions are already recognized by x_1,
so they are not counterexamples to recognition. They show why neither
ordinary low-degree hypotheses nor the pass89 homogeneous relation may
be silently inserted into the nonconical branch. The case f(t)=t is the
retained pass87 control; this family is an elementary extension, not an
example attributed to an external paper.

## 5. The localized fibration gate survives a free intrinsic action

The [quadratic-potential proof90](nonconical-quadratic-potential-pass90.md)
gives the actual equality \(A_\Omega=R_\Omega\), with two relative
generators over \(S_\Omega\). The precise sufficient conditions already
audited in [relative-hypersurface source gates79](relative-hypersurface-source-gates-pass79.md)
apply after this localization. Dutta's theorem, restated as Das--Dutta
Theorem 1.1(i), would give \(A_\Omega=S_\Omega[t]\) if its
height-one fibers were geometrically integral. Alternatively, Das--Dutta
Corollary 3.10 gives that conclusion from an \(S_\Omega\)-retraction,
using the already available flatness, generic polynomial line and domain
height-one fibers. The base is a UFD, and two relative generators make
the retraction kernel finitely generated. Neither missing premise follows
from the number of generators.[^fibration]

Even a fixed-point-free intrinsic LND does not supply these premises.
Localize the retained Weitzenbock control at its invariant \(\eta\):
\[
\begin{gathered}
C_0=\mathbb C[x,y,z],\quad \eta=xz-y^2,\quad
S_0=\mathbb C[x,\eta],\quad
D=x\partial_y+2y\partial_z,\\
C=(C_0)_\eta
=S_0[1/\eta][y,z]/(xz-y^2-\eta),\quad
\ker(D|C)=S_0[1/\eta],\\
1=\frac z\eta D(y)-\frac y{2\eta}D(z),\qquad
C^*=S_0[1/\eta]^*=\mathbb C^*\eta^{\mathbb Z},\\
C\otimes_{S_0[1/\eta]}\mathbb C(\eta)
=\mathbb C(\eta)[y,z]/(y^2+\eta)
=\mathbb C(\eta)(\sqrt{-\eta})[z]
\quad\text{at the divisor }x=0.
\end{gathered}
\tag{6}
\]
The invariant kernel is the retained explicit kernel, localized at an
invariant. The displayed unit identity proves fixed-point-freeness.
The total space is a smooth factorial principal open of an actual
polynomial three-ring. The polynomial \(\eta=xz-y^2\) is irreducible,
which gives the stated units. The relative relation is monic of degree
two in y, so C is free of rank two over \(S_0[1/\eta][z]\), and
faithfully flat over the base. Factorial closure makes every irreducible
base divisor remain prime in C. Thus the generic divisor fibers are
domains, but the last line of (6) is not geometrically integral.

There is also no base retraction: its proposed images of y and z would,
at x=0, give a Laurent polynomial square equal to \(-\eta\), impossible
by the odd \(\eta\)-valuation. Hence C is not a polynomial line over
this specified base. The example already has a quadratic relative
equation; a bound of degree at most three does not exclude it. This is
an intrinsic algebra control, not a realization of the extra original
nonconical frame or its determinant identities. Nor does the
contractibility of \(C_0\) establish contractibility of its principal
open C. Even a successful relative recognition on \(D(\Omega)\) would
still require descent across the removed divisor.

## 6. Search and access limits

The comparison first reread the retained
[mixed-time audit](mixed-time-degree-literature-addendum.md),
[pass85 source scope](rank-one-quasi-nice-source-scope-pass85.md), and
[pass79 exact-statement comparison](nice-good-recognition-source-scope-pass79.md).
Primary searches then combined quasi-nice, three time-linear coordinates,
constant acceleration, slice, four variables, homogeneous speed relation,
rank, and quadratic additive flow. Search snippets and secondary mirrors
were not used as mathematical authority. The selected current arXiv
records and the primary statements below were inspected directly.

No checked source directly recognizes (1), and no checked source makes
(4) automatic in the remaining nonconical case. This limited outcome
does not establish absence from the literature, validate novelty, or
replace independent expert review of the working pass89 proof. There was
no numerical run, external contact, or edit to pass89 or earlier files.

[^dl]: Dasgupta--Lahiri,
    [current record](https://arxiv.org/abs/2302.13787),
    [v6 primary PDF](https://arxiv.org/pdf/2302.13787v6).
    Freshly checked the version record, Definitions 2.2--2.3,
    Lemmas 2.9 and 2.12, and Theorem 5.2. The complete displayed
    proofs of Lemma 2.9 and Theorem 5.2 were read in the retained
    primary text `tmp/pdfs/general-dasgupta-lahiri-pass85.txt`.
    No full filtration-proof or original Wang-proof audit is claimed.

[^dg]: Dasgupta--Gupta,
    [*Nice derivations over principal ideal domains*, v1](https://arxiv.org/pdf/1701.03635v1).
    Fresh primary-text reads: rank definition, Theorems 3.1, 4.1 and 4.8,
    Corollary 3.8, and Proposition 4.4 with its complete displayed proof.
    These are exact primary restatements of Wang/Daigle where attributed,
    not fresh reads of those original proofs. Retained text:
    `tmp/pdfs/dg-nice-1701.03635v1.txt`.

[^bgl]: Bhatwadekar--Gupta--Lokhande,
    [*Some K-theoretic properties of the kernel of a locally nilpotent
    derivation on k[X1,...,X4]*, v1](https://arxiv.org/pdf/1501.01438v1),
    Theorem 3.5, PDF p.11. Its complete displayed statement and proof
    were freshly read in `tmp/pdfs/bgl-1501.01438v1.txt`; its DVR and
    local-global dependencies were not re-audited in full.

[^qt]: De Bondt,
    [*Quasi-translations and singular Hessians*, v1](https://arxiv.org/pdf/1501.05168v1),
    Proposition 1.3 and Remark 1.4, printed pp.4--5. Freshly read the
    complete displayed proof and preceding Lemmas 1.1--1.2 in
    `tmp/pdfs/bondt-1501.05168v1.txt`. No whole-paper audit is claimed.

[^dga]: Dasgupta--Gaifullin,
    [v2 primary HTML](https://arxiv.org/html/2306.00510v2),
    [version record](https://arxiv.org/abs/2306.00510).
    The record's latest version is v2, 9 December 2023. Freshly read
    Definition 2.9 and complete displayed statements/proofs of Theorem
    3.20, Proposition 4.1, Lemma 4.3, Corollary 4.4 and Theorem 4.5.
    Their invoked classification and kernel-intersection proofs were
    not freshly audited. No identity of numbering with the 2025 journal
    version is assumed.

[^strong]: De Bondt,
    [*Quadratic polynomial maps with Jacobian rank two*, v4](https://arxiv.org/pdf/1601.00579v4),
    definition, Lemma 1.2 and Proposition 1.3 on printed p.3.
    The complete displayed statement/proof was read in the primary text
    and visually checked on that page. Theorems 3.2--3.3 were checked
    for their exact statements; their full proofs are not newly claimed
    here. Proposition 1.3 itself has no quadratic-degree hypothesis.
    This consulted PDF is not added to the frozen durable source set.

[^fibration]: Das--Dutta,
    [*On codimension-one A1-fibration with retraction*, v1](https://arxiv.org/pdf/1302.5223v1),
    Theorem 1.1(i), Theorem 3.9 and Corollary 3.10, printed pp.2, 9--10.
    The exact statements and the complete displayed proof of Theorem 3.9
    were freshly read for this application boundary. Theorem 1.1 is the
    authors' explicit restatement of Dutta's 1995 result, not a fresh
    read of that original proof; the invoked patching dependencies were
    not re-audited in full. This is the retained pass79 source gate,
    not a new classification theorem.
