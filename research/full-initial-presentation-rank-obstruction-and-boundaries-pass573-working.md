# A full-initial presentation rank obstruction and its boundaries

Working general lemma: in an actual polynomial ring with a compatible
nonzero locally nilpotent derivation, adjoining the positive-degree
remainders of a homogeneous generating set of the FULL coordinate-initial
prime cannot leave the enlarged initial prime equal to the old extended
prime. A finite decreasing-weight proof gives the exact rank bound
\[
\boxed{r_{\rm enlarged}\le r_{\rm old}+q-1,}
\tag{1}
\]
where q is the number of full-ideal generators used.

The bound is sharp on an explicit actual translation frame. For a
higher-height initial prime, adjoining only one relation remainder can
raise the rank without contradiction. Generators obtained only after
localization also do not suffice. Degree-zero remainders have a different
terminal algebra and cannot be treated as positive-weight variables.

This is an initial-rank constraint, not a coordinate-descent theorem.
The numerical bound improves the automatic ambient-dimension bound only
at the complete-intersection generator count. In particular its direct
full-generator application does not improve that bound for the monomial
curve with degrees (4,5,6,7).

## 1. Actual ring, compatible filtration and full prime

Let K be a characteristic-zero field and let
\[
R=K[z_1,\ldots,z_n]\simeq K^{[n]}\ \subset\ \mathbb F[x],
\qquad n\ge2,
\tag{2}
\]
where the displayed z_i are actual polynomial coordinates, mathbb F is
a field extending K, and x is transcendental over mathbb F. Assume the
restriction to R of
\[
\Delta=g\partial_x,\qquad g\in\mathbb F^*,\qquad
\Delta|_{\mathbb F}=0
\tag{3}
\]
preserves R and is nonzero. It is then a K-LND on R: a sufficiently
high iterate kills every polynomial in mathbb F[x]. Its invariant
elements in R are exactly the elements of x degree zero, together
with zero. This compatibility is essential; a nonzero LND unrelated
to the x filtration is not enough.

The kernel contains a nonconstant element over K. More precisely it
has fraction-field transcendence degree n-1 over K. To recall the
local-slice proof, choose b with Delta squared b=0 and a=Delta b
nonzero. The element a is invariant and b/a is a slice in R_a.
The finite Taylor projection gives
R_a=(ker_R Delta)_a[b/a]. Passing to fraction fields proves the
transcendence-degree statement. No global slice or finite generation
of this kernel is required for the lemma below.

Put d_i=deg_x z_i and c_i=lc_x z_i, and assume EVERY d_i is positive.
For an independent initial variable eta define
\[
\begin{gathered}
S=K[\mathsf Z_1,\ldots,\mathsf Z_n],\qquad
\operatorname{wt}(\mathsf Z_i)=d_i,\\
\phi:S\longrightarrow\mathbb F[\eta],\qquad
\mathsf Z_i\longmapsto c_i\eta^{d_i},\qquad I=\ker\phi,\\
r=\operatorname{trdeg}_K\operatorname{im}\phi .
\end{gathered}
\tag{4}
\]
The ideal I is the FULL homogeneous initial prime, of height n-r.
It is nonzero: the positive-weight top of a nonconstant invariant's
unique source expression has zero initial image. Also r is at least
one, since a single nonzero c_i*eta to the positive d_i is transcendental
over K. No equality with the entire associated graded algebra of R is
asserted for the image in (4).

No equality Frac(R)=mathbb F(x), coefficient-field rationality, or
promotion of a coefficient to an actual coordinate is assumed.

## 2. Adjoining remainders of the full homogeneous ideal

Choose homogeneous generators
\[
I=(H_1,\ldots,H_q),\qquad
D_i=\operatorname{wt}H_i>0,
\quad f_i=H_i(z_1,\ldots,z_n),\quad e_i=\deg_x f_i<D_i.
\tag{5}
\]
Every f_i is nonzero because the z_i are actual polynomial coordinates
and H_i is a nonzero source polynomial. In this section assume also
that every e_i is POSITIVE. This is an additional condition, not a
consequence of (5).

Adjoin formal source variables, not actual coordinates:
\[
\begin{gathered}
S^+=S[\mathsf V_1,\ldots,\mathsf V_q],\qquad
\operatorname{wt}\mathsf V_i=e_i,\\
\operatorname{ev}:S^+\longrightarrow R,
\quad \mathsf Z_i\longmapsto z_i,
\quad \mathsf V_i\longmapsto f_i,\\
\ker\operatorname{ev}
 =(H_i-\mathsf V_i:1\le i\le q).
\end{gathered}
\tag{6}
\]
The last equality follows by eliminating the monic linear variables
V_i, after which the original-coordinate evaluation S to R is an
isomorphism. Thus (6) is an exact actual presentation, although none
of the f_i is asserted to be a coordinate.

If b_i is the x-leading coefficient of f_i, let
\[
\phi^+:S^+\longrightarrow\mathbb F[\eta],\qquad
\mathsf Z_i\longmapsto c_i\eta^{d_i},\quad
\mathsf V_i\longmapsto b_i\eta^{e_i},\qquad I^+=\ker\phi^+.
\tag{7}
\]
This is again the FULL initial prime. It contains I*S^+.
The claim is
\[
\boxed{I S^+\subsetneq I^+.}
\tag{8}
\]

Suppose instead equality holds. Fix a nonconstant invariant f in R,
so deg_x f=0 and f is not in K. Start with any source representative
P in S^+ of f; one is its original polynomial expression in the z_i.
If its top weight is M>0, write its nonzero homogeneous top as Q.
The coefficient at x to the M in the evaluated P, multiplied by
eta to the M, is phi^+(Q).
Since f has degree zero, Q belongs to I^+=I*S^+.

Full ideal generation in (5) therefore gives
\[
Q=\sum_{i=1}^q A_iH_i,\qquad
\operatorname{wt}A_i=M-D_i
\quad\text{for every nonzero }A_i.
\tag{9}
\]
The A_i may involve all the V variables. To obtain (9), take any
ideal expression for Q and project each coefficient to its required
homogeneous weight. Negative required weights contribute zero.
This uses full ideal membership, not divisibility by one selected
factor and not membership only after localization.

Replace the representative by
\[
P_{\rm new}=P-\sum_i A_i(H_i-\mathsf V_i).
\tag{10}
\]
Its evaluation is still exactly f. All of the old weight-M part
cancels, while
wt(A_i V_i)=M-D_i+e_i<M. Every other old term already had weight
less than M. The maximum source weight has therefore strictly
decreased.

All source weights are positive integers. Repetition of (10)
terminates after finitely many steps at a representative of weight
zero, which is a K-constant. This contradicts f not in K. A zero
representative is likewise impossible for this nonzero f. This proves
(8) without a finite SAGBA basis, a termination conjecture, or an
unproved coordinate completion.

Since I*S^+ is a prime of height n-r and I^+ is a strictly larger
prime in the polynomial ring of dimension n+q, (8) gives
\[
\operatorname{trdeg}_K\operatorname{im}\phi^+
 \le n+q-(n-r+1)=r+q-1.
\tag{11}
\]
Equivalently, the q new initials are not algebraically independent
over the fraction field generated by the old initials.

## 3. Dimension and the complete-intersection limitation

There is also an automatic bound
\[
\operatorname{trdeg}_K\operatorname{im}\phi^+\le n.
\tag{12}
\]
Indeed any algebraically independent subset of the finitely many
initial generators comes from algebraically independent actual
polynomials. A nonzero polynomial relation among their actual
polynomials would, on taking its top weighted part, contradict
independence of their initials. Such a subset can have at most n
members in the actual R of transcendence degree n.

The height theorem gives q at least n-r for a generating set in (5).
Use the smallest homogeneous generating set for the best bound.
At the complete-intersection generator count q=n-r, (11) improves
(12) to n-1. No regular-sequence assertion is needed in its proof.
If q>n-r, however, r+q-1 is at least n, and (11) gives no stronger
NUMERICAL rank bound than (12). Redundant ideal generators only
weaken it. This limitation does not disappear by calling a subset
of the ideal a full presentation.

Now take K=C. After harmless nonzero complex rescalings of the source
variables, the concrete monomial-curve map is
\[
K[\mathsf X,\mathsf Y,\mathsf Z,\mathsf W]
 \longrightarrow K[\eta],\qquad
(\mathsf X,\mathsf Y,\mathsf Z,\mathsf W)
 \longmapsto(\eta^4,\eta^5,\eta^6,\eta^7).
\tag{13}
\]
Its full prime has height three. There is no nonzero relation of
weight less than ten. The repeated-weight monomials through weight
twelve are exactly
\[
\begin{array}{c|c|c}
\text{weight}&\text{monomials}&\text{relation-space dimension}\\\hline
10&\mathsf Y^2,\ \mathsf X\mathsf Z&1\\
11&\mathsf Y\mathsf Z,\ \mathsf X\mathsf W&1\\
12&\mathsf X^3,\ \mathsf Z^2,\ \mathsf Y\mathsf W&2.
\end{array}
\tag{14}
\]
Below ten, the positive attainable weights are four through nine,
with the unique monomials X,Y,Z,W,X squared,XY respectively.
The smallest positive source weight is four. Thus multiplication
of any nonzero ideal element by the homogeneous maximal ideal has
weight at least fourteen. The four independent relation directions
in (14) survive independently in I/(X,Y,Z,W)I. Every generating set
therefore has at least four members, not three.

Here r=1 and q is at least four, so (11) is no stronger numerically
than the automatic upper bound four. This is the precise limitation
at the degree tuple used in
[562](rank-sensitive-cofactors-and-rank-one-semigroup-boundary-pass562-working.md)
and the actual controls
[565](rank-one-semigroup-minimal-actual-translation-controls-pass565-working.md).
The argument concerns their full monomial-curve ideal; it does not
declare an abstract tuple to be a globally minimizing actual frame.

## 4. An actual sharp full-generator control

In the known translation ring C[a,b,c,u], take K=C, Delta=partial_u and
put
\[
P=a+u^2,\quad B=b+cu,\quad C=c+au,\qquad
(X_1,X_2,X_3,X_4)=(P,P+B,P+C,P+B+C+u).
\tag{15}
\]
Here C in (15) is an intermediate polynomial, not a constant field.
The complete polynomial inverse is
\[
\begin{aligned}
U&=X_4-X_2-X_3+X_1,\\
A&=X_1-U^2,\\
C_0&=X_3-X_1-AU,\\
B_0&=X_2-X_1-C_0U,\\
(a,b,c,u)&=(A,B_0,C_0,U).
\end{aligned}
\tag{16}
\]
Substitution of (15) into (16) gives successively u,a,c,b.
Conversely substitution of (16) into (15) first recovers P=X1,
B=X2-X1 and C=X3-X1, and then X4. This proves both inverse orders
on the entire fourfold, without a localization.

All four degrees are two, with leader one. Their full initial prime
and a homogeneous generating set are
\[
I=(H_1,H_2,H_3),\qquad
H_1=\mathsf X_2-\mathsf X_1,\quad
H_2=\mathsf X_3-\mathsf X_1,\quad
H_3=\mathsf X_4-\mathsf X_1.
\tag{17}
\]
The quotient identifies all four source variables and injects by
X1 mapping to eta squared, so (17) is the FULL prime of rank one.
The actual remainders all have positive degree one:
\[
\begin{aligned}
f_1&=b+cu,&\operatorname{in}(f_1)&=c\eta,\\
f_2&=c+au,&\operatorname{in}(f_2)&=a\eta,\\
f_3&=b+c+(a+c+1)u,&\operatorname{in}(f_3)&=(a+c+1)\eta.
\end{aligned}
\tag{18}
\]

If ONLY f1 is adjoined, the enlarged initial field has rank two:
eta squared and c*eta are algebraically independent. After imposing
the old ideal (17), their source is K[X1,V1], and its map is
injective. Thus the enlarged full initial prime is exactly the
old extended I. This is a genuine actual countercontrol to a
single-remainder rank-rise obstruction for a higher-height I.
The failure of the proposed reduction is precise: H2 and H3 are
not generated by H1, so an arbitrary invariant top cannot be
reduced by H1-V1 alone.

If ALL three remainders are adjoined, their initial field is
C(eta,a,c), of transcendence degree three. Indeed
\[
\eta=\operatorname{in}(f_3)-\operatorname{in}(f_1)-\operatorname{in}(f_2),
\quad c=\operatorname{in}(f_1)/\eta,\quad
a=\operatorname{in}(f_2)/\eta.
\tag{19}
\]
These are identities in an initial fraction field, not actual
coordinate maps using divisions. They also prove algebraic
independence of the three new initials.

The FULL enlarged initial prime is
\[
I^+=\bigl(H_1,H_2,H_3,
\mathsf X_1-(\mathsf V_3-\mathsf V_1-\mathsf V_2)^2\bigr).
\tag{20}
\]
The displayed quotient is a polynomial ring in the three V variables,
whose initial images are independent by (19); hence no relation is
missing. Its rank is three, exactly r+q-1=1+3-1. The new relation
in (20), evaluated ENTIRELY in the actual ring, has remainder
\[
X_1-(f_3-f_1-f_2)^2=a,
\qquad \deg_u a=0.
\tag{21}
\]
This control attains the full-generator bound. It is an already
polynomial translation frame, also used for a different leading-field
purpose in
[566](rank-one-maximal-cofactor-leading-line-boundary-pass566-working.md).
It is not globally minimizing, and no such claim is made.

## 5. Saturation or multiples do not replace full generation

Use a second actual translation frame in the same known polynomial ring:
\[
(T_1,T_2,T_3,T_4)=(u,a+u^2,b+u^3,c+u^4).
\tag{22}
\]
Its entire inverse is u=T1, a=T2-T1 squared, b=T3-T1 cubed,
c=T4-T1 to the fourth. All degrees are positive, namely (1,2,3,4),
and the full initial prime is
\[
I=(G_2,G_3,G_4),\qquad
G_i=\mathsf T_i-\mathsf T_1^i\quad(2\le i\le4).
\tag{23}
\]
The quotient is K[T1], mapping injectively to K[eta].

Choose instead the three homogeneous relations H_i=T1*G_i.
Their source weights are i+1, and their evaluated remainders are
\[
(H_2(T),H_3(T),H_4(T))=(au,bu,cu),
\tag{24}
\]
all of exact degree one. The enlarged initial field is generated by
eta,a*eta,b*eta,c*eta. These four elements are algebraically independent:
their fraction field is C(eta,a,b,c), with the inverse field identities
a=(a eta)/eta and similarly for b,c. Equivalently their full Jacobian
in eta,a,b,c has determinant eta cubed. The entire enlarged initial
prime is therefore exactly the extension of (23).

Thus the initial rank rises from one to four even though all three
adjoined cancelled-relation remainders have positive smaller degrees.
There is no conflict with (8):
\[
(H_2,H_3,H_4)=\mathsf T_1 I\ne I,\qquad
(\mathsf T_1 I:\mathsf T_1^{\infty})=I.
\tag{25}
\]
The strictness follows, for example, from G2 not being divisible
by T1. The saturation equality follows because I is prime and
T1 is not in I. These H_i generate I after inverting T1, but
NOT in the original polynomial source. Reducing the invariant
a, whose source top is G2, would require division by T1.
That is precisely the unlicensed step. No actual boundary is
deleted in this control.

## 6. The degree-zero boundary

In the same actual frame (22), adjoin the remainders of the TRUE
full generators G2,G3,G4 themselves. They are a,b,c, all of degree
zero. The enlarged initial field has rank four, and its full prime
is again just the old extended ideal (23): the remaining initial
images eta,a,b,c are independent.

Now the new source variables have weight ZERO. A decreasing-weight
argument can end in K[V2,V3,V4], not merely K. In fact
\[
\ker_R\partial_u=\mathbb C[a,b,c]
\tag{26}
\]
is exactly that terminal algebra in this example. It would be false
to use it as a contradiction.

There is a precise general version of this observation. If some e_i
in (5) are zero, keep the same presentation and assume I^+=I*S^+.
The proof (9),(10) still decreases every POSITIVE source weight.
It stops at a polynomial in only the zero-weight V variables.
Conversely each such actual f_i is killed by Delta. Consequently
under that equality hypothesis it proves exactly
\[
\ker_R\Delta=K[f_i:e_i=0],
\tag{27}
\]
not ker_R Delta=K. No actual coordinate status of those f_i is
inferred from this statement. Equations (22)--(26) demonstrate
why the positivity condition in the main rank obstruction matters.

## 7. What this does and does not give for actual descent

The principal full-prime case has q=1, so (8) recovers the finite
positive-weight remainder argument without a higher-height
substitution. At higher height, every invariant top must be
covered by the whole ideal used in (9). A chosen factor, one
relation, or a localized generating set cannot supply that step.

More generally, for a finite positive-weight presentation of the
actual R with actual relation ideal J, its weighted initial ideal
in_w(J) is contained in the full kernel of the map to actual initials.
If equality held, the same argument would reduce every nonconstant
Delta-invariant representative by actual relations until it were
constant. Therefore this containment must be strict in the present
compatible setting. In making this deduction one uses the FULL
initial ideal in_w(J), not just the listed leading forms of selected
defining relations. Homogeneous membership gives a finite sum of
leading forms of actual relations of the matching weight; subtracting
the corresponding actual relations strictly lowers weight exactly
as in (10).

These restrictions do not produce an elementary coordinate replacement.
A remainder may involve all original coordinates, and its actual
partial in a proposed replaced slot need not be a complex unit.
The exact descent criterion in
[569](rank-one-cancellation-remainder-coordinate-obstruction-pass569-working.md)
instead uses membership of that coordinate's leading form in the FULL
embedded associated graded of the other-coordinate subalgebra.
This source proves no such membership for an arbitrary minimizing
frame. Source569 also supplies an actual low-degree cancellation
remainder whose entire gradient obstructs any coordinate completion.

The explicit controls here have known polynomial invariant rings and
explicit lower frames. They do not assert a globally minimizing
all-positive frame, a counterexample to entry, or a classification
of other degree-lowering automorphisms. No finite-generation or
termination assertion for a general coordinate-descent procedure is
hidden in the finite fixed-representative proof (10).

## 8. Verification and scope

The target was checked absent before creation, and the writing guide
was read completely. Fresh unsaved9af105 verifies both inverse orders
of (15),(16), every degree and leader in (18), the exact entire
remainder (21), the independence Jacobians, and the complete evaluated
remainders in (24). Its low-weight support listing agrees with the
explicit argument (14). These are fresh polynomial checks, not saved
checker executions. The full ideal identifications and finite-weight
proofs are supplied above rather than inferred from numerical samples.
Post-writing fresh c98d9a rechecks both complete inverse orders for
both actual frames, the entire added relation (20), its exact remainder
(21), all degree and leader statements, and the independence Jacobians.

Only this new source was created. No prior source or canonical record
was edited. No saved checker was executed, imported or compiled.
Complete self-read through EOF and an independent saved-source review
are separate from the outline checks. There is no novelty, global
degree-minimum, coordinate-entry, recognition or unrestricted
cancellation claim.
