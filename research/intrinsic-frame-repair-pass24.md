# Genuine tangent syzygies: exact extraction and a six-generator obstruction

There is already a finite construction of a nonzero locally nilpotent
member of the slice's tangent-module syzygies. It is a reformulation of
the established leading-derivation argument, not a new recognition
theorem. What it does not produce is a slice or a proper intrinsic
action.

A different natural repair fails decisively: none of the six canonical
Koszul tangent generators need be locally nilpotent, even when the
slice is an explicit polynomial coordinate, all six generators are
primitive, and every generator genuinely descends to the section.
The counterexample below is not constant-coefficient projection or a
curvature calculation. All its fields annihilate the slice exactly.

This pass gives the full module identities, the exact counterexample,
and the published-hypothesis boundary for a successful construction.
It does not disprove the existence of other useful polynomial
combinations, prove failure of every frame, or settle cancellation.

## 1. The genuine tangent module and its canonical generators

Let

\[
B=\mathbb C[x_1,x_2,x_3,x_4]=A[s],\qquad E(s)=1,
\qquad E|_A=0.
\tag{1}
\]

Set T_i=partial_{x_i}, s_i=T_i(s), and e_i=E(x_i). Then
sum e_i*s_i=1, so the gradient row of s is unimodular. Define

\[
\mathcal T_s=\{V\in\operatorname{Der}_{\mathbb C}(B):V(s)=0\},
\qquad K_{ij}=s_iT_j-s_jT_i\quad(i<j).
\tag{2}
\]

Every K_{ij} annihilates s, so it preserves (s) and induces a
derivation of A identified with B/(s). This descent is automatic
for these fields. It does not assume local nilpotence.

The six K_{ij} generate the entire B-module T_s. Indeed, for
V=sum v_j*T_j with sum v_j*s_j=0, the exact identity is

\[
V=\sum_{i<j}(e_i v_j-e_j v_i)K_{ij}.
\tag{3}
\]

Expanding the right side gives
(sum e_i*s_i)V-(sum v_i*s_i)E=V. The coefficients are actual
polynomials in B, with no restriction to the old invariant frame.

Every derivation of A lifts to T_s. Lift its values on the images
of x_i to coefficients v_i in B. The resulting ambient V has
V(s)=sq for some q in B. Replacing V by V-sqE preserves its
residue and makes its value on s zero. The kernel of reduction
T_s->Der(A) is s*T_s: if V=sW and V(s)=0, the domain condition
forces W(s)=0. Therefore

\[
\operatorname{Der}_{\mathbb C}(A)
\cong\mathcal T_s/s\mathcal T_s.
\tag{4}
\]

This is a genuinely descending presentation of every intrinsic
derivation, not merely three selected algebraically independent
invariants or an ambient tangent projection.

## 2. A nonzero tangent LND is already constructible

Choose an ambient coordinate partial T that moves A. Such a partial
exists: otherwise every element of A would belong to the common
kernel of all four coordinate partials, which is C. Let q be the
highest s-degree of its horizontal restriction to A. The earlier
[leading-symbol proof](intrinsic-actions-pass.md) gives

\[
T|_A=\sum_{j=0}^{q}s^jD_j,\qquad
0\ne D_q\in\operatorname{LND}(A),\qquad
\deg_s T(s)\le q.
\tag{5}
\]

Write h_q for the coefficient of s^q in T(s). Since commutation
with E differentiates coefficient functions with respect to s,

\[
U=\frac{1}{q!}\operatorname{ad}_E^q(T)
=\widetilde D_q+h_qE,
\qquad
V=U-U(s)E=\widetilde D_q.
\tag{6}
\]

Here the tilde means the coefficientwise extension to A[s] killing
s. Thus V is an actual nonzero LND of B, V(s)=0 and [V,E]=0.
Equation (3) expresses it as a polynomial combination of the K_{ij}.
All operations in (6) are finite and polynomial; there is no division
by the slice or extension across an unproved pole locus.

Subtracting a vertical component is not safe for an arbitrary
derivation. It is valid in this specific formula because the highest
commutator has exactly the coefficientwise form in (6), with D_q
already proved locally nilpotent. This is the exceptional verified
case, not the general projection rule refuted in earlier passes.

The associated-graded theorem underlying (5) is established
literature.[^leading] Neither a uniform bound on q nor a proper
action is part of it. The prior
[primitive leading control](leading-derivation-pass23.md) already
shows that D_q can be primitive, have fixed points and have no slice.
Thus finding some locally nilpotent tangent combination is not the
unresolved existence step. Recognizing a sufficiently strong one is.

## 3. An explicit coordinate slice with no locally nilpotent Koszul generator

In B=C[x_1,x_2,x_3,x_4], put

\[
a=x_1+x_4,\quad b=x_2+x_4,\quad c=x_3+x_4,
\qquad s=x_4-a^2-b^2-c^2.
\tag{7}
\]

These are genuine polynomial coordinates. If Q=a^2+b^2+c^2,
their inverse is

\[
x_1=a-s-Q,\quad x_2=b-s-Q,\quad
x_3=c-s-Q,\quad x_4=s+Q.
\tag{8}
\]

The coordinate translation holding a,b,c fixed is

\[
E=-T_1-T_2-T_3+T_4,
\qquad A=\ker E=\mathbb C[a,b,c].
\tag{9}
\]

Its slice gradient is

\[
(s_1,s_2,s_3,s_4)=(-2a,-2b,-2c,1-2a-2b-2c).
\tag{10}
\]

Every K_{ij} from (2) annihilates s. Here each also commutes with E,
because its coefficients in (10) are invariant and the T_i commute
with this constant E. Thus these examples do not fail the descent
condition from the preceding pass.

Write a_1=a,a_2=b,a_3=c, and let k_{ij} be the induced field on A.
For 1<=i<j<=3,

\[
k_{ij}=2a_j\partial_{a_i}-2a_i\partial_{a_j}.
\tag{11}
\]

For 1<=i<=3,

\[
k_{i4}=
\left(2\sum_{j\ne i}a_j-1\right)\partial_{a_i}
-2a_i\sum_{j\ne i}\partial_{a_j}.
\tag{12}
\]

All six fields are primitive. In (11) the two nonzero coefficients
are independent coordinate variables up to units. In (12) the gcd
of a_i and 2*sum_{j ne i}a_j-1 is one. The same coprimality holds
for their ambient coefficient pairs in (10).

Nevertheless none is locally nilpotent. The exact recurrences are

\[
k_{ij}^{\,2}(a_i)=-4a_i\quad(j\le3),\qquad
k_{i4}^{\,2}(a_i)=-8a_i.
\tag{13}
\]

For every m>=1 their even iterates are respectively (-4)^m*a_i
and (-8)^m*a_i, which are nonzero polynomials. Thus all six
canonical module generators fail local nilpotence, despite exact
descent, primitivity and the strongest possible coordinate-slice
hypothesis. Dividing a common coefficient cannot repair them.

This refutes the specific proposed shortcut that some canonical
Koszul tangent generator must provide the required intrinsic LND.
It also shows that primitive normalization of those generators does
not supply a fallback. It does not refute the existence of other
members of their span, which (6) already guarantees.

## 4. Successful combinations exist in the control, not by a general rule

The counterexample deliberately retains an exact positive control.
Directly from (11)--(12),

\[
\begin{aligned}
\partial_a&=k_{12}+k_{13}-k_{14},\\
\partial_b&=-k_{12}+k_{23}-k_{24},\\
\partial_c&=-k_{13}-k_{23}-k_{34}.
\end{aligned}
\tag{14}
\]

These three combinations are commuting coordinate partials. In
this explicitly known polynomial quotient, the bad generating set
can therefore be repaired. The proof does not assert that constant
combinations always suffice, or that this particular example defeats
every possible polynomial choice of coefficients.

For a hypothetical unknown A, equation (3) supplies a spanning
module and equation (6) supplies a nonzero LND. Neither supplies
the analogue of the three slice coordinates in (14). Local
nilpotence, pointwise generation and a coordinate slice are distinct
requirements even when the candidate fields truly descend.

## 5. The exact published-hypothesis boundary

For the stably affine threefold A in (1), the following condition
would finish recognition:

\[
\exists V\in\operatorname{LND}(B),\quad V(s)=0,
\quad\exists g\in B:\ V(g)=1.
\tag{15}
\]

Indeed V descends to an LND of A=B/(s), and the residue of g is
an intrinsic slice. The slice theorem makes its action a translation
over an affine quotient. Its action graph is a closed immersion into
the product over C, so the action is proper. Gurjar--Masuda--Miyanishi
Theorem 4.1.1 then applies: a stably affine threefold with a proper
Ga-action is affine three-space.[^proper]

Conversely, if A is polynomial, extend one of its coordinate
partials to B by killing s. It satisfies (15). Thus (15) is an
equivalent recognition target in this setting, not a consequence
of a free tangent module. In particular, merely replacing
"find coordinates" by "find a sliced LND among tangent syzygies"
does not prove the required existence.

The weaker nonzero-LND statement in (6) remains useful but does not
meet the properness hypothesis. A derivation that sends one function
to one must also be proved locally nilpotent before its action or
the slice theorem can be invoked. No such property is inferred from
coprime coefficients or a unimodular module basis here.

## 6. Exact controls and scope

An independent inline SymPy command checked the coordinate inverse,
E(s)=1, K_{ij}(s)=0 for every pair, all six induced fields, their
coefficient gcds, both square-iterate identities in (13), and all
three successful combinations in (14). It completed in 0.056
seconds of measured script time. The all-iterate non-nilpotence
assertion follows from the written recurrence, not finite sampling.
A separate model audit independently reconstructed the six fields,
their recurrences, coefficient coprimality and the unimodular
syzygy-generation hypothesis, with no defect found.
No new regression suite or test-method count is introduced.

The genuine module and highest-commutator identities have proofs
above. The only recognition theorem invoked has its proper-action
and stable-affineness hypotheses stated explicitly. No existing
report, registry, or old checker was edited, and no classification
claim for all tangent combinations is made.

The bounded outcome is therefore exact: nonzero intrinsic tangent
LND extraction is already possible, canonical primitive tangent
generators can all fail, and a sliced tangent LND would close the
problem but has not been constructed universally.

[^leading]: B. Alhajjar, [*LND-Filtrations and Semi-Rigid Domains*](https://arxiv.org/pdf/1501.00445), Proposition 2.2 and Proposition 3.4, with Daigle and Makar-Limanov credit retained. Their primary statements were read in the preceding pass; the argument used here is the same one already written in the project.

[^proper]: R. V. Gurjar, K. Masuda and M. Miyanishi, [*Affine Space Fibrations*, primary author text](https://oa.tib.eu/renate/bitstreams/2db0f47c-00f9-4195-9c8a-a46722165a99/download), Theorem 4.1.1, printed p. 44. Its statement and following proof setup were read directly in this pass: X must be affine of dimension three, satisfy X times affine (n-3)-space is affine n-space for n>=4, and carry a proper additive action. The theorem is not being applied to an unsliced or merely primitive tangent field.
