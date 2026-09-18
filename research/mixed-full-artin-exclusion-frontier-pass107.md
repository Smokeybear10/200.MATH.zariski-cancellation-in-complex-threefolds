# A mixed-fiber branch is excluded by the actual quartic algebra

Within the supplied nonconical quadratic frame, a collapsed mixed
fiber with nonzero speed normal cannot have a full three-dimensional
second-degree residue image. Its second-degree image must have
dimension two. This closes one branch left open in106, without
assuming that its point-supported image ideal is reduced.

The result does not solve complex-threefold cancellation. The
two-dimensional second-degree branch, whole-double fibers, zero
speed normal, global recognition, and entry from an arbitrary
sliced action remain unresolved. The intended complex-threefold
interpretation of Professor Luo's email is also unconfirmed.

## 1. Precise setting

The actual algebra has a polynomial cylinder and the supplied
original quadratic-coordinate frame. Its intrinsic invariant base
is S=C[s1,s2], and its primitive locally nilpotent derivation N
has full kernel S. The actual inclusion S into A is faithfully
flat. Over K=Frac(S), the ring A becomes the polynomial line K[v].

At the chosen closed base point m, the whole fiber is
D[c], with D=C[G]/(G²(G−1)). This is a doubled line and a
separate simple line, including the nilpotent structure. The
speed-normal coefficient L(m) is nonzero. Define F_j=ker N^(j+1),
I_j=N^j(F_j), and W_j as the image of F_j in the whole fiber.
The retained results give W2 contained in D and its dimension
equal to two or three. They also give the actual generation
A=S[A1,A2,c], with A1,A2 in F2 and c in F4.[^setting]

All subsequent closed-point modules are localized over R=S_m.
The proof assumes W2=D and derives a contradiction. It does not
assume that the three independent fiber residues are a polynomial
coordinate system or that a degree module commutes with reduction.

## 2. Exact algebra at a quadratic constant divisor

The first new input is a complete local classification over a
base DVR V with uniformizer p. The generic algebra is K[v], the
whole special fiber is k'[w] with [k':k]=2, the induced derivation
is nonzero, and an actual degree-two element has nonconstant
residue. The last condition comes from the good-generator
noncollapse theorem in the current frame.[^divisor]

If I1=p^eV, a minimal first-degree element r has derivative p^e.
Its residue generates the quadratic constants. The surviving
second-degree element then supplies an exact presentation

\[
B=V[r,t]/(p^e t-r^2-ar-b),\qquad
Nr=p^e,\quad Nt=2r+a,
\]

where the reduced quadratic is irreducible. Alternating monomials
t^i and rt^i give a basis in every degree. Thus

\[
I_j=p^{e\lceil j/2\rceil}V.
\]

This is an equality for the whole localized algebra and all
degrees, not a calculation in its completion. The two saved
derivations construct the presentation independently. The
selected quartic c has its sharp fourth-image valuation only
after the additional mixed-sector boundary condition is used.

## 3. From divisor multiplicities to point-supported ideals

Suppose W2=D. Let I1=PR. The exact divisor valuations and the
full-Artin module result106 give

\[
I_2=PJ_2,\qquad I_3=P^2R,\qquad I_4=P^2J_4,
\]

where J2 and J4 are proper maximal-primary two-generated
complete intersections. Both previously undetermined scalar
matrix factors are units. The ideal constraints include
J2² contained in J4 and P in J2J4.[^ideals]

With F2=R+Rz+Rw and r=az+bw, the ideal J2 is exactly (a,b).
The conic identity is

\[
\epsilon r^2-2B_2z+2B_1w=Q,
\qquad P=aB_1+bB_2,\quad\epsilon\in R^*.
\]

The important new point is that the coefficients belong to J2²,
not merely to m². A finite free piece with independent closed
residues inside a flat module is pure: its intersection with
HA equals H times that piece for every ideal H. Applying this
standard consequence of Lazard's theorem to F2 and H=J2² proves
B1,B2,Q in J2², and P in J2³.[^purity]

Thus the next construction works even when (a,b) is nonreduced.
Replacing an ideal by its radical would not justify this step.

## 4. Two actual quartics and a unit determinant

Write B1,B2,Q as quadratic expressions in a,b and collect the
conic as a²Qaa+abQab+b²Qbb=0. Flatness preserves the regular
sequence a,b. Reduction modulo a and modulo b therefore gives
actual elements U=Qbb/a and V=Qaa/b of A_R. They have degree
four and satisfy

\[
N^4U=6\epsilon^3aP^2,\qquad
N^4V=6\epsilon^3bP^2,\qquad
N^3(bU-aV)=-6\epsilon^2P^2.
\]

The last identity makes bU-aV a generator of F3/F2 up to a
unit, because I3=P²R. The coordinate matrix of U,V in the free
rank-two module F4/F2 has unit determinant. This follows from
the normalized fourth-derivative row and the identity
XJX^t=(det X)J for the alternating two-by-two matrix J.
Consequently F4=F2 direct-sum RU direct-sum RV and J4=J2.
No reduced-ideal dichotomy is used.[^quartic]

The final quartic proof also derives I3=P² directly from this
actual cubic combination and normalizes its fourth-image row
directly at height one. Thus the exclusion does not require the
separate106 nonprincipality theorem or assume I3 is principal.

## 5. The fiber-dimension contradiction

The algebra K4=R[F4] has the exact three-equation presentation

\[
K_4=R[Z,W,U,V]/
(bV-Q_{aa},\ aV+bU+Q_{ab},\ aU-Q_{bb}).
\]

The equations have the correct generic and height-one
localizations. Their raw closed fiber is S0[U,V], where S0
is generated by 1,Z,W as a vector space. Independent actual
residues identify S0 with D. The height bound rules out vertical
minimal primes; the complete-intersection argument rules out
embedded associated primes. This proves the exact presentation,
rather than assuming that three displayed relations generate
the entire kernel.[^quartic]

It follows that K4/mK4 is D[U,V], of dimension two. But the
actual frame gives A_R=R[F4], while its whole fiber D[c] has
dimension one. This contradiction excludes W2=D. Therefore
the remaining mixed branch has dim W2=2.

## 6. Verification and remaining questions

The universal claims have written proofs and separate AI
reconstructions. The finite checkers cover conic identities,
derivative constants, determinant certificates and explicit
nonreduced parameter substitutions. They cannot certify
flatness, the source frame, universal presentation exactness,
or cancellation. The canonical execution and exact file versions
are recorded in [capture107](verification-pass107-working.json)
and [checkpoint107](checkpoint-pass107-working.json).

The canonical run passes four suites and seven methods: two new
finite controls and five retained quartic checks. The recorded
process wall time is 1.821055458 seconds; unittest reports
1.398 seconds. Historical full-suite results were not rerun.

An explicit replica of the quadratic derivation changes the
valuation formula but kills its special-fiber action. A cubic
constant extension has a different formula and no surviving
second-degree parameter. These controls omit named hypotheses;
neither is an actual-frame or cancellation counterexample.

The next bounded mathematical task is the rank-two W2 branch.
It lacks the full F2 residue independence used by purity, so
the argument cannot simply be repeated there. One must identify
the missing residue direction and its first actual lift.

There is a useful starting constraint. In this branch W2 is the
span of 1,G. A nonconstant first-degree residue would make
1,r,r² three independent second-degree residues, since G has
minimal polynomial of degree three. Hence W1=C, as already
recorded in105. Choose F2=R+RG+RH with H having zero whole
residue, and shift the first-degree generator to r=aG+bH
with zero residue. Then a belongs to n, whereas b need not.
The conic gives B1,B2 in n and
Q+2B2G=epsilon r²+2B1H in n²A_R. Purity applies to the
rank-two piece R+RG, so Q,B2 lie in n² and
P=aB1+bB2 lies in n². This does not make B1 lie in n²,
make J2 proper, or give purity of the full F2. These missing
implications remain explicit. The other scope gaps listed at
the beginning remain separate.

No human expert review, formal Lean verification, or comprehensive
novelty clearance is claimed. This remains private working
research, with no contact, posting, or submission.

## Sources

[^setting]: [Actual degree-two Artin image104](mixed-degree-module-artin-image-pass104.md); [third-degree image105](mixed-third-degree-image-pass105.md), including its actual generating set; [rank defect105](mixed-cubic-rank-defect-pass105.md); [full-Artin module106](mixed-full-artin-two-generator-pass106.md).

[^divisor]: [Actual divisor91](nonconical-residue-degree-bound-pass91.md), specialized to the current quadratic frame; [exact filtration107](quadratic-constant-divisor-filtration-pass107.md); [independent DVR proof107](quadratic-divisor-normal-form-gates-pass107.md).

[^ideals]: [Normalized image ideals107](mixed-normalized-image-ideals-pass107.md).

[^purity]: [Residue-basis purity107](residue-basis-purity-pass107.md), with the Stacks Project's [Lazard theorem, 058G](https://stacks.math.columbia.edu/tag/058G) and [factorization proof, 058C](https://stacks.math.columbia.edu/tag/058C), consulted September 14, 2026.

[^quartic]: [Generalized full-Artin exclusion107](mixed-full-artin-quartic-exclusion-pass107.md). Its predecessor is [quartic fiber52](quartic-fiber-gate-pass52.md), whose reduced-point assumption is replaced here by the proved all-ideal purity and unit-determinant argument. The presentation uses [Stacks 02JN](https://stacks.math.columbia.edu/tag/02JN), [00N6](https://stacks.math.columbia.edu/tag/00N6), and [0BUS](https://stacks.math.columbia.edu/tag/0BUS), consulted September 14, 2026.
