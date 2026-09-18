# Three-quasi-nice recognition and inner-closure source scope

The bounded primary-source check on 14 September 2026 did not locate
a theorem recognizing every sliced four-variable action with three
time-linear coordinates and one time-quadratic coordinate. The nearby
recognition results still require an actual invariant coordinate or
an actual polynomial presentation over an invariant base. This is a
statement-applicability audit, not an exhaustive absence or novelty claim.

The strict containment proved in pass84 is exactly the existing notion
of inner integral closure. That identification supplies terminology
and closure-theoretic consequences, but not polynomial membership in
the selected good-speed ideal. The full image ideals of the original
sliced derivation are already unit ideals and are different objects.

## 1. The precise action being compared

Retain the actual coordinates and supplied polynomial slice:
\[
\begin{gathered}
B=\mathbb C[x_1,x_2,x_3,z],\qquad E\in\operatorname{LND}(B),
\qquad E(s)=1,\\
E^2x_i=0\ (1\le i\le3),\qquad E^2z=q,\qquad E(q)=0,\\
A=\ker E,\qquad a_i=E(x_i),\qquad
I=(a_1,a_2,a_3)B.
\end{gathered}
\tag{1}
\]
The definition of m-quasi-niceness in Dasgupta--Lahiri, Definitions
2.2--2.3, applies with m=3, n=4 and base field C: the second iterate
kills three actual coordinate generators. It does not require any
first iterate to vanish. Strict three-quasi-niceness would additionally
exclude every coordinate system making the action nice. A nonzero q
in (1) does not establish that coordinate-independent exclusion.[^dl]

This audit rereads and updates the exact target in the retained
[mixed-time-degree addendum](mixed-time-degree-literature-addendum.md).
No ordinary spatial-degree bound follows from (1). Neither q times
partial_z nor the full acceleration coefficient field may be assumed
to be a commuting LND, as the actual
[pass81 controls](acceleration-field-obstruction-pass81.md) demonstrate.

## 2. Recognition statements retain genuine coordinate hypotheses

Dasgupta--Gupta's Theorem 4.1 reproduces Wang's two-quasi result on
an actual three-variable polynomial ring over a characteristic-zero
field. Their Theorem 4.8 reproduces Daigle's result starting with one
coordinate Y satisfying DY nonzero and D squared Y zero, again in
three variables. Proposition 4.4 instead assumes an actual
R[X,Y,Z], a PID R fixed by D, irreducibility, and generic case (I)
of Theorem 4.1. None is a four-variable theorem obtained by simply
renaming one invariant as a base parameter.[^dg]

The same paper's Corollary 3.8 assumes an actual invariant coordinate
X_1 and D squared X_i zero for i=2,3,4. It therefore requires full
niceness as well as the invariant-coordinate gate, not (1) alone.

The more directly relevant Bhatwadekar--Gupta--Lokhande Theorem 3.5
requires D(T)=0 in actual coordinates B=k[T,X,Y,Z] and regularity
of ker D, and gives ker D=k[T]^[2].[^bgl] In (1), the slice supplies
regularity: A=B/(s), and the equation E(s)=1 makes the partial
derivatives of s generate the unit ideal. It does not supply the
invariant ambient coordinate T. This separates the missing premise
from the hypotheses already available.

For example, there is a standard genuinely applicable conditional
case. If the actual good-coordinate subring is stable, then
\[
R_0=\mathbb C[x_1,x_2,x_3],\qquad
E(R_0)\subseteq R_0
\quad\Longleftrightarrow\quad
\partial_z a_i=0\text{ for all }i.
\tag{2}
\]
The restriction is an actual nice LND of R_0. If it is zero, x_1 is
an invariant ambient coordinate. Otherwise Dasgupta--Gupta's Theorem
3.1(i), which has no irreducibility premise, gives a nonzero invariant
constant linear form in x_1,x_2,x_3. That form is an actual ambient
coordinate, so Theorem 3.5 just cited recognizes the original kernel.
This is an application of established results, not a new recognition
family.

The known inclusion partial_z(a_i) in I is weaker than (2). Indeed,
the actual two-speed control of the
[pass84 checker](strict_slice_checks_pass84.py) has coordinates
(A,X,Y,Z), slice s=Z-XY, and good velocities
(0,A,X-As). Its third good velocity has Z-derivative -A, not zero.
The control is already recognized, but shows that (2) is not automatic
in the supplied frame. A generic invariant field or a localized
polynomial chart is likewise not (2).

## 3. Image ideals are not the selected speed ideal

The currently checked Dasgupta--Lahiri record is arXiv:2302.13787v6,
dated 24 July 2026. Lemma 2.12 concerns an irreducible R-LND on an
actual R[X,Y] over a UFD; its kernel descriptions require that
polynomial presentation first. Theorem 4.1 computes image ideals for
nice relative two-variable actions. Theorem 5.2 assumes a non-fixed-
point-free, strictly one-quasi-nice relative action, with an irreducible
first velocity in R. The original E in (1) is fixed-point-free, so
that latter theorem does not apply to E.[^dl]

More basically, Lemma 2.9 and its elementary proof give, in our notation,
\[
\mathcal I_j(E):=A\cap E^j(B)=A\quad(j\ge1),
\qquad
E^j\!\left(\frac{c s^j}{j!}\right)=c\quad(c\in A).
\tag{3}
\]
The three chosen velocities generate only I_A=(a_1,a_2,a_3)A.
They need not generate the full plinth or any full image ideal in (3).
For instance the retained sliced action
E=a squared partial_x+(1+ax)partial_z has selected ideal (a squared)
in its actual four-variable ring, while (3) still holds. Multiplying or
dividing E by invariant factors creates a different derivation; its
image ideals cannot be substituted for those of E without a new
comparison argument.

## 4. Exact relation to existing inner integral closure

Epstein--Hochster Theorem 5.4(1),(3) identifies monic coefficient
orders J^(j+1) and a power r^N in J^(N+1) with inner integral
closure, denoted J_(>1). Their Definition 5.9 defines natural
closure by J-natural=J+J_(>1). This is not the assertion that
J_(>1) is contained in J, or that every ideal is naturally closed.[^eh]

The actual [strict-slice proof](rank-one-strict-slice-certificate-pass84.md)
provides an explicit exponent N=(deg_x s-1) squared when q is nonzero
and I is proper. Its result also descends to the invariant ring:
\[
q^N\in I^{N+1},\qquad
B=A[s],\quad I=I_A B
\quad\Longrightarrow\quad
q^N\in I_A^{N+1},\qquad q\in(I_A)_{>1}.
\tag{4}
\]
Indeed a_i and q belong to A, and evaluation at s=0 contracts every
extended ideal power exactly. This uses the actual slice presentation,
not an assumption that A is a polynomial three-ring.

Consequently, natural closedness of I_A would suffice for q in I_A,
equivalently q in I. That is an additional ideal hypothesis, not a
conclusion of the source. General ideal countercontrols from
[pass84](embedded-square-ideal-boundary-pass84.md) already prevent
turning the strict condition alone into first- or square-power
membership. They are not action realizations.

Theorem 5.6 of Epstein--Hochster also gives inner containment in
continuous closure over an affine complex algebra. Here A is affine
because A=B/(s). In particular, the source gives continuous functions
c_i on the complex points of Spec A satisfying
\[
q=\sum_{i=1}^3 c_i a_i.
\tag{5}
\]
Continuous coefficients need not belong to A. Equation (5) is neither
a polynomial shear nor an ideal-membership proof. The earlier
elementary strict-slice proof does not use this continuous-closure
theorem, its valuations, or its auxiliary graded-ring argument.

## 5. Bounded search and source-access record

Queries combined locally nilpotent derivation, three-quasi-nice,
(n-1)-nice, global slice, four variables, quadratic flow, image ideals,
inner integral closure and natural closure. Retained source notes
were checked first. Search results were used to locate primary papers,
not as substitutes for theorem hypotheses. Unrelated Lie-algebra and
noncommutative nilpotence results were discarded.

The new comparison does not reveal a published source deriving an
invariant coordinate from (1), making its selected speed ideal
naturally closed, or converting (4) into recognition. This states
only what was and was not located in this bounded check. It does
not establish historical novelty, certify a complete literature
corpus, or resolve cancellation. No external contact, checker run,
shared metadata change, or edit to pass84 or earlier accompanies
this note.

[^dl]: Nikhilesh Dasgupta and Animesh Lahiri,
    [current arXiv record](https://arxiv.org/abs/2302.13787) and
    [version-six PDF](https://arxiv.org/pdf/2302.13787v6).
    The landing-page title ends *over a UFD*; the PDF title ends
    *on R[X1,X2]*. The version/date, Definitions 2.2--2.3,
    Lemmas 2.9 and 2.12, and Theorems 4.1 and 5.2 were freshly
    checked. The complete short proof of Lemma 2.9 was read;
    this is not a fresh audit of every theorem proof or of the
    original Wang paper underlying Lemma 2.12.

[^dg]: Nikhilesh Dasgupta and Neena Gupta,
    [*Nice derivations over principal ideal domains*](https://arxiv.org/pdf/1701.03635v1),
    [published DOI](https://doi.org/10.1016/j.jpaa.2018.02.025).
    Freshly read Theorems 3.1, 4.1 and 4.8, Corollary 3.8,
    and Proposition 4.4 with its complete displayed proof.
    Wang's and Daigle's original proofs reproduced as statements
    were not freshly read. Their scopes are not generalized here.

[^bgl]: S. M. Bhatwadekar, Neena Gupta and Swapnil A. Lokhande,
    [*Some K-theoretic properties of the kernel of a locally nilpotent
    derivation on k[X1,...,X4]*](https://arxiv.org/pdf/1501.01438v1),
    Theorem 3.5. The exact statement and complete displayed proof
    on PDF page 11 were freshly read, not its entire predecessor
    chain or the whole paper.

[^eh]: Neil Epstein and Melvin Hochster,
    [*Continuous Closure, Axes Closure, and Natural Closure*](https://sites.lsa.umich.edu/hochster/wp-content/uploads/sites/1337/2024/08/CnClTAMS.pdf).
    Freshly read the definition before Theorem 5.4, its complete
    displayed statement and proof on printed pp.20--21, the
    complete displayed statement and proof of Theorem 5.6 on
    pp.21--22, and Definition 5.9 on p.23. The previous valuation
    theorem and Theorem 2.5 used in those proofs were not newly
    audited. This is a precise published-theorem application, not
    a new proof of their general closure theory.
