# Priority comparison for the two-remainder coefficient classification

Date: 2026-09-13. This is a bounded comparison of the closest already
recorded primary statements, not a fresh database-wide novelty search.

Conclusion: the canonical derivations, their exceptional geometry, and
the general modification-lifting machinery have definite published
predecessors. The translation theorems read here do not automatically
give the complete two-remainder classification in the physical ring.
That is a statement about the hypotheses actually checked, not evidence
that the classification is new. Mathematical priority remains unresolved.

## 1. Exact target and definite inherited credit

The [pass-23 theorem](polynomial-local-slice-coefficients-pass23.md) fixes
n >= 1, f=xz-y^2, a=f^n, nu=2n+1,
r=x^3+ay, h=a^2*z+2a*x^2*y+x^5, p=ah, and D=-Jac(f,h,.).
For each b in C[f,h,r], it sets F=int_0^r b(f,h,v)dv and c=b(0,0,0).
Its precise criterion for E=D+b*partial_t on C[x,y,z,t] is

\[
c\ne0,\qquad
F(0,h,r)\bmod(r^5-h^3)=cr+H_f(h),
\qquad
F(f,0,r)\bmod(r^2+f^\nu)=cr+H_h(f).
\]

Every positive case is asserted to have polynomial kernel and explicit
translation coordinates. Both negative tests rule out every slice
degree. These are the statements being compared, not just local
nilpotence or generic triviality.

Dasgupta--Gaifullin's Theorem 5.7 contains the entire canonical base:
take m=2 and their F(t_1,t_2)=t_1^2. Their local-slice relation,
irreducibility, minimality, kernel and rank-three conclusions give the
base data, with the sign of the Jacobian reversed here. The displayed
construction and the full proof of Theorem 5.7 were reread. This
three-variable theorem does not itself state the added-coefficient
classification above.
[Primary author text, Section 5](https://arxiv.org/html/2306.00510v2).

Freudenburg's Section 8.2 is exactly the n=1 base. Its degree modules,
modification sequence, and five-orbit versus two-orbit exceptional
fibers are published material. In particular the two exceptional
branches and their residue relations are not newly discovered geometry.
Section 9 instead gives a sliced triangular extension on five-space,
with invariant added coefficient 1+f+f^2, and Question 9.3 asks about
its relative polynomial kernel. That example is not literally the
present physical four-space extension. No nonconjugacy or absence of
a more elaborate specialization is inferred.
[Primary author text, Sections 8.2 and 9](https://arxiv.org/pdf/1602.08786).

Kaliman--Zaidenberg Proposition 2.1 lifts a homomorphism of affine
triples when the full center ideal maps into the target ideal and the
denominator maps to a unit multiple of the target denominator.
Corollary 2.2 gives the automorphism version with equality of ideals.
These statements, reread with their hypotheses, are the inherited
lifting principle. They require the full ideals, not just their
reduced supports, and do not construct an ideal-preserving map.
[Primary manuscript, Section 2](https://arxiv.org/pdf/math/9801076).
The project's exact two-stage application remains documented in the
[pass-20 reduction](priority-boundary-pass20.md). The finite curve
congruences in the present proof fulfill that obligation; they do not
create a new universal lifting principle.

## 2. The three presentations must not be interchanged

Write S=C[f,h], keeping f,h independent in the first presentation.

| Presentation | Dimension over C | Role |
| --- | --- | --- |
| S[x,r,t] | 5 | Relative polynomial three-space |
| S_0[t]=S[x,r,t]/(xh-r^2-f^nu) | 4 | Invariant hypersurface quotient |
| R[t]=C[x,y,z,t] | 4 | Actual physical polynomial ring |

The final ring contains S_0[t] but also its divided physical
coordinates y=(r-x^3)/f^n and
z=(h-2f^n*x^2*y-x^5)/f^(2n). These are a genuine overring passage,
not three independent variables over S. In particular R[t] is not
S^[3]; its generic relative dimension over S is two.

The raw auxiliary derivation is triangular, indeed twin-triangular:

\[
\mathcal E=ah\partial_r+2ar\partial_x+b(f,h,r)\partial_t
\quad\hbox{on }S[r,x,t].
\]

The equation xh-r^2=f^nu and the physical overring are additional
conditions. Neither triangularity in this auxiliary presentation nor
an arbitrary coordinate theorem on it automatically passes through
both operations.

There is also a direct ambient-coordinate obstruction for the old
invariant plane. At x=y=z=0, both df and dh vanish in physical
four-space. Hence dG(f,h)=0 there for every G in C[f,h]. A polynomial
coordinate cannot have a critical point, since its coordinate
projection is smooth. Thus no element of this old invariant plane
is an ambient coordinate of R[t]. This does not exclude the new
invariant coordinates produced by the positive proof outside that plane.

## 3. What the general translation theorems require

Dubouloz--Finston--Jaradat's main theorem assumes a proper locally
triangulable action on a Zariski locally trivial A^3-bundle over a
Noetherian normal characteristic-zero base. Its conclusion is an
A^2-bundle quotient after excluding codimension at least two in that
base. Their Dedekind-base corollaries yield global translations, and
therefore every proper triangular action on ordinary A^4 is a
translation. These primary statements and the definition of local
triangularity were reread on printed pages 1962-1963. Proposition 3.1
also retains a triangular polynomial-three-space presentation over a
DVR; it does not concern arbitrary modified hypersurfaces.
[Published paper](https://msp.org/ant/2014/8-8/ant-v8-n8-p06-s.pdf).

Our deductions from those hypotheses are specific. The auxiliary base
Spec S has dimension two, so the Dedekind conclusion cannot be used
there. On physical four-space, f does not give an A^3-bundle: its
zero fiber is the singular threefold
Spec C[x,y,z,t]/(xz-y^2). Nor does the printed physical derivation
come with a triangular coordinate presentation. Constructing one would
permit the theorem to apply, but is not supplied by calling f,h,r
coordinates. The positive construction eventually supplies actual
translation coordinates; using them retroactively is not an independent
derivation of the two tests.

Kaliman's Theorem 0.1 requires a proper action on C^4 preserving an
ambient polynomial coordinate. It then gives translation coordinates.
The stronger fibration formulation, Theorem 0.2, retains explicit
generic-quotient and fiber hypotheses; Corollary 0.3 assumes smooth
contractible fibers. These hypotheses were reread, not replaced by
the existence of two invariant polynomials.
[Published paper, Theorems 0.1-0.2 and Corollary 0.3](https://msp.org/ant/2018/12-2/ant-v12-n2-p01-s.pdf).

A slice gives a globally trivial additive bundle over its kernel and
therefore properness. It does not by the slice theorem alone identify
that kernel with C^[3]. The old invariant-plane calculation in Section 2
shows precisely why f, h, or a polynomial recombination of them cannot
be used as Kaliman's ambient coordinate. Corollary 0.3 also fails its
smooth-fiber hypothesis for this f. No general replacement base function
or complete verification of Theorem 0.2 is asserted here.

The algebraic companion has the same coordinate premise:
Bhatwadekar--Gupta--Lokhande Theorem 3.5 treats a nonzero
k[T]-linear LND on k[T,X,Y,Z] with regular kernel and concludes
that kernel is k[T]^[2]. Its full statement and proof were reread.
[Primary author text, Theorem 3.5](https://arxiv.org/html/1501.01438v1).
In our slice-positive cases regularity is available, but T must first
be an actual ambient invariant coordinate. Section 2 rules out taking
T from the old plane. This is a missing hypothesis in a shortcut, not
a claim that no such coordinate exists in the positive cases.

## 4. A concrete control: properness does not transfer to the raw auxiliary ring

The distinction above is stronger than a count of variables. Take

\[
b=1+5hr^4,\qquad F=r+hr^5.
\]

Its two remainders are r+h^4 and r, respectively. Its physical action
has a slice independently of the full classification proof. Indeed put

\[
g_0=\frac{r^5-h^3-f^{2\nu}r}{p}
 =-h(x^2y+az)-2x f^{n+1}r\in R,
\]
\[
H=hg_0+f^{2\nu-n}r.
\]

Differentiating the numerator identity gives
D(g_0)=5r^4-f^(2nu), hence D(H)=5hr^4. Thus s=t-H is a
polynomial slice. In the coordinate system R[s], E=D+partial_s,
and its finite D-flow supplies three invariant polynomial coordinates.
So the physical action is a translation without appealing to the
new all-coefficient criterion.

By contrast, the raw auxiliary action has fixed points at
f=0, h=1, r^4=-1/5, with x,t arbitrary. All its coefficients vanish
there. Taking x=r^2 puts these points on the invariant quadratic
level as well. Thus even that hypersurface action has fixed points,
although the physical action is a translation. A fixed-point additive
action is not proper, since its stabilizer is the nonproper group A^1.

The extra points do not represent physical points: at f=0,h=1
the physical identities give r^5=1, incompatible with r^4=-1/5.
Consequently properness, freeness, or a slice on the physical overring
cannot simply be asserted on the raw auxiliary presentation. The
polynomial gauge, which may use elements outside S_0, and the physical
modification genuinely matter. Fourteen inline exact scalar controls
checked the two remainders, the displayed derivative cancellation, and
the auxiliary zero coefficients; these are not test-method counts.

## 5. Reading boundary and disposition

The primary passages actually reread were Dasgupta--Gaifullin's
construction, Corollary 5.6 and Theorem 5.7 with proof; Freudenburg's
Section 8.2 formulas, degree modules and exceptional fibers, and the
complete displayed extension and question at the end of Section 9;
the 2014 translation theorem and its corollaries; Kaliman's
Theorems 0.1-0.2 and Corollary 0.3; Bhatwadekar--Gupta--Lokhande
Theorem 3.5 with proof; and Kaliman--Zaidenberg's lifting statements.

Freudenburg's 2009 full example section was not retrieved or retried.
The [previous access record](priority-comparison-pass21.md) remains in
force: the available abstracts do not print the theta_n formulas needed
for an exact specialization test. This comparison neither rules out
coverage by that paper nor claims a collision. No broad database
search, blocked-access workaround, credentials, purchase, or external
contact was used.

The checked general theorems do not automatically supply the two
coefficient tests on the physical ring, and Section 4 decisively rules
out one tempting transfer of their properness hypothesis. A different
published normal form or a valid additional reduction could still make
the classification a consequence of existing results. Therefore the
packet must retain definite inherited credit and the label
**priority unresolved**, with no assertion of novelty or general
cancellation. No other project file or registry was changed.
