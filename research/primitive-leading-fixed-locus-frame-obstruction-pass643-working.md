# A full coordinate frame with a common primitive leading fixed locus

Date: September 18, 2026.

There is an actual polynomial coordinate frame on
\(B=A[u]=\mathbb C[a,b,c,u]\), with \(E=\partial_u\), such that
every nonzero constant coordinate-translation direction has the same
primitive intrinsic leading derivation
\[
 D=a\partial_b+b\partial_c.
 \tag{1}
\]
It vanishes on the whole line \(a=b=0\). More generally, Section 5
realizes any prescribed nonzero primitive LND on a polynomial
three-ring as the primitive top of every constant direction of a
single whole ambient frame. The conclusion survives any
finite sequence, applied to one such direction, of individual invariant
replicas and conjugations by \(\exp(vE)\), \(v\in A\). Thus the unit
determinant of a full commuting ambient frame does not force these
primitive leading extractions to move a given point.

This is a boundary for a specified extraction procedure. The base is
already \(\mathbb C^{[3]}\), and the inverse coordinate map below supplies
an explicit nonlinear repair. No point in this example is fixed by
every intrinsic LND. The result does not assert failure under arbitrary
nonlinear reframing, conjugation by other automorphisms, or recombination
of different transformed directions. General cancellation remains
unresolved; novelty is not asserted.

## 1. Exact extraction and vertical-shift formulas

For this section let \(A\) be a finitely generated domain over a
characteristic-zero field and let \(B=A[u]\). Suppose \(\delta\) is an LND of \(B\) whose
restriction to \(A\) is nonzero. Write its finite horizontal expansion
as
\[
 \delta|_A=\sum_{j=0}^{q}u^jD_j,
 \qquad D_q\ne0,
 \qquad \delta(u)=k(u).
 \tag{2}
\]
Each \(D_j\) is a derivation of \(A\). The inherited leading-derivation
lemma gives \(D_q\in\operatorname{LND}(A)\) and
\(\deg_u k\le q\). These are statements about the highest coefficient,
not about arbitrary lower coefficients. The associated-graded argument
and actual counterexamples to lower-coefficient extraction are recorded
in [23](leading-derivation-pass23.md) and the
[filtration note](filtration-obstruction-pass.md).

For completeness, the bound on the vertical coefficient follows from
the same graded argument. The filtration shift is
\(\max(q,\deg_u k-1)\). If \(\deg_u k>q\), the induced homogeneous
LND would send the initial variable \(\eta\) to a nonzero multiple of
\(\eta\). An LND on a characteristic-zero domain cannot do this:
\(L(x)\in xR\) implies \(L(x)=0\), by additivity of LND degree on
products. This contradicts the nonzero vertical initial coefficient.

Consequently the highest adjoint extraction, followed by removing its
vertical component, is exactly
\[
 \frac{1}{q!}\operatorname{ad}_E^q\delta
   =\widetilde D_q+k_qE,
 \qquad k_q=[u^q]k,
 \qquad \operatorname{ad}_E^{q+1}\delta=0.
 \tag{3}
\]
Here \(\widetilde D_q\) extends \(D_q\) and kills \(u\). In particular,
the nonzero horizontal term fixes the highest adjoint order even if the
top vertical coefficient is zero.

Let \(v\in A\), set \(\phi_v=\exp(vE)\), and use the convention
\(\delta^{(v)}=\phi_v\delta\phi_v^{-1}\). The exact whole formulas are
\[
 \begin{aligned}
 \delta^{(v)}|_A&=\sum_{j=0}^q(u+v)^jD_j,\\
 \delta^{(v)}(u)&=k(u+v)-\sum_{j=0}^q(u+v)^jD_j(v).
 \end{aligned}
 \tag{4}
\]
Thus the horizontal degree remains \(q\), the highest intrinsic
coefficient remains \(D_q\), and the top vertical coefficient becomes
\(k_q-D_q(v)\). This holds identically on \(A\), not just at a
specified point. These vertical shifts commute, so sequences containing
only such shifts merely add their parameters.

There is also an exact replica rule. If \(0\ne h\in\ker\delta\), write
\(h=u^r h_r+\) lower terms, with \(h_r\in A\setminus\{0\}\). Then
\[
 (h\delta)|_A
   =u^{q+r}h_rD_q+\text{lower horizontal terms},
 \qquad D_q(h_r)=0.
 \tag{5}
\]
The invariant condition proves that \(h\delta\) is LND. The second
assertion follows by taking the coefficient of \(u^{q+r}\) in
\(\delta(h)=0\): its vertical contribution has degree at most
\(q+r-1\), or is zero when \(r=0\). Neither (4) nor (5) promotes a
lower coefficient to an LND.

## 2. The whole polynomial frame and its inverse

Use the specific polynomial base \(A=\mathbb C[a,b,c]\), and let
\(D\) be (1), extended to kill \(u\). Define
\[
 \alpha=a,
 \qquad \beta=b-au,
 \qquad \gamma=c-bu+\frac{au^2}{2},
 \qquad F(\alpha,\beta,\gamma)
      =\alpha\gamma^2+\beta\gamma^3+\gamma^5,
 \qquad U=u+F.
 \tag{6}
\]
Then \((\alpha,\beta,\gamma,U)\) is an actual coordinate system of
\(B\). Its entire polynomial inverse is
\[
 \begin{aligned}
 u&=U-F(\alpha,\beta,\gamma),\\
 a&=\alpha,\\
 b&=\beta+\alpha\bigl(U-F(\alpha,\beta,\gamma)\bigr),\\
 c&=\gamma+\beta\bigl(U-F(\alpha,\beta,\gamma)\bigr)
       +\frac{\alpha}{2}\bigl(U-F(\alpha,\beta,\gamma)\bigr)^2.
 \end{aligned}
 \tag{7}
\]
Both inverse compositions follow by substitution: first undo the
\(U\)-shear, then the triangular \((a,b,c)\)-change. Thus polynomiality
does not rest on the Jacobian conjecture or an assigned leading frame.
Both successive changes have Jacobian determinant one.

Put \(T=D+E\). It kills \(\alpha,\beta,\gamma\) and sends \(u\) to
one. Before the \(U\)-shear, the three other partials are
\[
 A_0=\partial_a+u\partial_b+\frac{u^2}{2}\partial_c,
 \qquad B_0=\partial_b+u\partial_c,
 \qquad C_0=\partial_c.
 \tag{8}
\]
The actual partials in the final frame are therefore
\[
 \begin{aligned}
 T_\alpha&=A_0-\gamma^2T,\\
 T_\beta&=B_0-\gamma^3T,\\
 T_\gamma&=C_0-
    (2\alpha\gamma+3\beta\gamma^2+5\gamma^4)T,\\
 T_U&=T.
 \end{aligned}
 \tag{9}
\]
They are commuting LNDs because they are genuine coordinate partials.
Their coefficient determinant in \((a,b,c,u)\) is one. Equations
(6)--(9) give the entire fields, including their vertical components.

## 3. Every constant direction has the same primitive top

The exact horizontal degrees and intrinsic leading coefficients in (9)
are
\[
 \begin{array}{c|c|c}
 \text{field}&\text{horizontal }u\text{-degree}&
       \text{highest intrinsic coefficient}\\ \hline
 T_\alpha&4&-\dfrac{a^2}{4}D\\
 T_\beta&6&-\dfrac{a^3}{8}D\\
 T_\gamma&8&-\dfrac{5a^4}{16}D\\
 T_U&0&D.
 \end{array}
 \tag{10}
\]
Indeed \(\gamma\) has degree two and leading coefficient \(a/2\).
In \(F_\gamma\), the terms \(2\alpha\gamma\) and
\(3\beta\gamma^2\) have degrees at most two and five, whereas
\(5\gamma^4\) has degree eight. The old fields (8) have degrees at
most two. This proves every entry of (10) without cancellation.

Let
\[
 T_{\mathbf c}
  =c_1T_\alpha+c_2T_\beta+c_3T_\gamma+c_4T_U,
 \qquad 0\ne\mathbf c\in\mathbb C^4.
 \tag{11}
\]
It is again an actual coordinate partial after an invertible constant
linear change of the final coordinates. The four degrees in (10) are
distinct. The unique greatest degree among its nonzero summands
therefore cannot cancel, so its intrinsic top is a nonzero scalar
multiple of exactly one of the four listed fields.

The nonzero coefficients of \(D\) are \(a,b\), whose gcd is one.
Consequently the primitive part of every top in (11) is \(D\), up to
a nonzero complex scalar. This covers every nonzero constant translation
in the entire affine-linear orbit of this frame, not only its four
displayed basis vectors.

The field \(D\) is LND: its flow is
\[
 (a,b,c)\longmapsto
 \left(a,\ b+ta,\ c+tb+\frac{t^2a}{2}\right).
 \tag{12}
\]
Its fixed scheme has ideal \((a,b)\); in particular it fixes the line
\(\Lambda=\{a=b=0\}\) pointwise and has no slice. Primitivity has
already removed every common polynomial coefficient, so this fixed
locus is not an artifact of a removable leading multiplier.

The determinant comparison is explicit. At any
\((a,b,c,u)=(0,0,c_0,u_0)\), the four whole fields in (9) have columns
\[
 \begin{pmatrix}
 1&0&0&0\\
 u_0&1&0&0\\
 u_0^2/2&u_0&1&0\\
 -c_0^2&-c_0^3&-5c_0^4&1
 \end{pmatrix}.
 \tag{13}
\]
This matrix has determinant one, while all four primitive intrinsic
tops vanish at the underlying point \((0,0,c_0)\). Evaluation and
taking a highest coefficient need not preserve degree or rank in the
same way; the lower terms provide the full ambient tangent frame.

## 4. The exact closure under replicas and vertical shifts

Start with any single \(T_{\mathbf c}\) from (11). At each subsequent
step permit either of the following operations on the current LND
\(\delta\):

- replace it by \(h\delta\), where \(0\ne h\in\ker\delta\);
- replace it by \(\exp(vE)\delta\exp(-vE)\), where \(v\in A\).

Every field in any finite sequence is nonzero and locally nilpotent.
Its highest horizontal coefficient has the form
\[
 cD,
 \qquad 0\ne c\in\ker_A D.
 \tag{14}
\]
For the initial field this follows from (10). If (14) holds, (4) leaves
\(cD\) unchanged. Under a replica, (5) replaces it by \(h_rcD\) and
gives \(cD(h_r)=0\). Since \(A\) is a domain, \(D(h_r)=0\).
This proves (14) by induction, including replicas followed by shifts,
shifts followed by replicas, and arbitrarily interleaved finite words.

The gcd of the nonzero coefficients of \(cD\) is \(c\), up to a unit,
because \(\gcd(a,b)=1\). Thus all these primitive tops still equal
\(D\) up to scalar and still vanish on \(\Lambda\). More generally,
even regular rational multiples within this one intrinsic line cannot
help:
\[
 (\operatorname{Frac}(A)D)\cap\operatorname{Der}_{\mathbb C}(A)
       =AD.
 \tag{15}
\]
If a reduced denominator of a rational multiplier gives a regular
field, it divides both \(a\) and \(b\), and hence is a unit. The
one-line saturation argument itself is inherited from
[28, Section 4](canonical-top-pass28.md).

The quantifier is important. Constant combinations are allowed in the
initial frame as in (11). The induction does not allow arbitrary sums
or brackets of separately transformed fields, nor conjugation by
arbitrary ambient automorphisms. Such operations require their own
local-nilpotence and extraction arguments. Lower coefficients are not
claimed to be LNDs.

## 5. Every primitive LND on a polynomial three-ring can occur this way

The same construction has a general form. Let
\(A=\mathbb C[y_1,y_2,y_3]\) and let \(0\ne D\in\operatorname{LND}(A)\)
be primitive. After an invertible constant linear choice of the three
coordinates, assume
\[
 \deg_D y_1=\deg_D y_2=\deg_D y_3=N\ge1.
 \tag{16}
\]
This choice is always possible. Start with any linear coordinate span,
let \(N\) be its maximal \(D\)-degree, and choose a linear basis outside
the proper subspace killed by \(D^N\). Over the infinite field
\(\mathbb C\), that complement contains a basis. No nonlinear
classification of \(D\) is being assumed.

On \(B=A[u]\), extend \(D\) to kill \(u\), and set
\[
 c_i=\exp(-uD)y_i,
 \qquad F(c_1,c_2,c_3)=c_1^4+c_2^5+c_3^6,
 \qquad U=u+F(c_1,c_2,c_3).
 \tag{17}
\]
The exponential is finite on each polynomial. It is an actual
\(\mathbb C[u]\)-automorphism with inverse \(\exp(uD)\), followed by
the polynomial \(U\)-shear. To write the whole inverse without any
variable-parameter ambiguity, let
\(\Phi_i(\tau;Y)=\sum_j\tau^jD^j(y_i)(Y)/j!\) be the finite
constant-parameter flow polynomial, using an independent triple
\(Y=(Y_1,Y_2,Y_3)\). The inverse of (17) is
\[
 u=U-F(c_1,c_2,c_3),
 \qquad
 y_i=\Phi_i\bigl(U-F(c_1,c_2,c_3);c_1,c_2,c_3\bigr).
 \tag{18}
\]
The two inverse compositions follow first from the opposite finite
flows with \(u\) held independent and then from the inverse shear.

Each \(c_i\) has exact \(u\)-degree \(N\), with nonzero coefficient
\[
 \ell_i=\frac{(-1)^N}{N!}D^N(y_i)\in\ker_A D.
 \tag{19}
\]
Let \(J=(\partial c_i/\partial y_j)\), with \(u\) fixed. Its entries
have \(u\)-degree at most \(N\). The flow and its polynomial inverse
show that \(\det J\) is a polynomial unit; at \(u=0\) it is one.
Thus \(\det J=1\), and each entry of \(J^{-1}\), a two-by-two
cofactor, has degree at most \(2N\).

The coordinate partials \(T_i^0=\partial_{c_i}\) in the pre-shear
frame \((c_1,c_2,c_3,u)\) have these inverse-Jacobian columns as their
horizontal coefficients and kill \(u\). Their horizontal degrees are
therefore at most \(2N\). The fourth partial, holding the \(c_i\)
fixed, is \(T=D+E\). Writing \(n_1=4,n_2=5,n_3=6\), the final
coordinate partials are exactly
\[
 T_i=T_i^0-n_i c_i^{n_i-1}(D+E),
 \qquad T_U=D+E.
 \tag{20}
\]
They have horizontal degrees and tops
\[
 \begin{array}{c|c|c}
 T_1&3N&-4\ell_1^3D\\
 T_2&4N&-5\ell_2^4D\\
 T_3&5N&-6\ell_3^5D\\
 T_U&0&D.
 \end{array}
 \tag{21}
\]
The three positive degrees strictly exceed \(2N\), so the old
partials cannot cancel these terms. The four degrees are distinct,
which proves that every nonzero constant combination has primitive top
\(D\) up to scalar. The invariant coefficients in (19) also verify
the starting hypothesis for the finite-operation induction of Section
4. That proof applies verbatim to this arbitrary primitive \(D\).

In particular, if the prescribed \(D\) has a nonempty fixed locus,
every primitive top arising by the specified operations fixes that
same locus. This construction does not require \(D\) to have a slice,
to be triangular in the chosen coordinates, or to have any specified
rank or plinth. Conversely it makes no claim that an arbitrary
stably polynomial base has coordinates \(y_1,y_2,y_3\): polynomiality
of \(A\) is an explicit input to this realization control.

## 6. Nonlinear repair, deduplication, and remaining scope

The explicit inverse (7) returns the adapted coordinates
\((a,b,c,u)\). Their three horizontal partials
\(\partial_a,\partial_b,\partial_c\) are commuting intrinsic LNDs
with no common fixed point. In particular \(\partial_a\) moves every
point of \(\Lambda\). This nonlinear change succeeds, so the control
does not suggest that \(A\) has a genuine all-LND-fixed point or a
nontrivial Makar-Limanov invariant.

The bounded archive comparison is as follows. The
[filtration note, Section 5](filtration-obstruction-pass.md) already has
a full actual frame with equal raw leading fields \(2a\partial_c\),
all vanishing on \(a=0\); their primitive part is free.
[32, Section 3](stable-polynomial-invariants-pass32.md) covers every
constant direction of another full frame, but again the primitive top
is \(\partial_c\). Individual primitive nonsliced tops and their
one-line saturation are already present in
[23](leading-derivation-pass23.md), [28](canonical-top-pass28.md), and
[29](horizontal-selection-pass29.md). These antecedents are not being
claimed anew. The additional tested scope here is the common fixed
locus of the primitive tops for every constant direction of one full
frame, together with the exact finite-operation statement of Section 4
and the arbitrary-\(D\) realization of Section 5.
This is a project-local deduplication claim, not a literature-priority
claim.

The [fixed-base result 640](fixed-base-critical-locus-obstruction-pass640-working.md)
and [intrinsic symmetry result 641](kaliman-intrinsic-ml-recognition-pass641-working.md)
motivate testing extraction at a hypothetical common fixed point.
They are not needed to prove this control. A true point fixed by every
intrinsic LND would, by definition, also kill every extracted leading
LND. The present example only proves that the invertibility of one
whole ambient frame, primitive normalization, individual replicas, and
vertical shifts do not by themselves contradict such leading-value
vanishing. A proof using the stronger all-intrinsic-fixed hypothesis
must add an argument not supplied by those operations.

## 7. Verification and status

The explicit control was derived in this pass; a separate agent supplied
the arbitrary-\(D\) realization, which was independently reconstructed
by the author and the root reviewer at argument level. A fresh unsaved
symbolic calculation reconstructed both entire inverse compositions, determinant
one, all coordinate-partial pairings, all sixteen ordered frame
brackets, and every degree and leading coefficient in (10). Further
fresh checks verified a complete interleaving of two invariant replicas
and two vertical shifts, and both inverse compositions and every
coordinate-partial identity for an \(N=1\) instance of Section 5. A separate
agent independently reconstructed the coordinate shear and the
distinct-degree argument before this note was held. The finite-word
claim is proved by (4)--(5) and induction, not by testing finitely many
replicas or shifts. No saved checker was run, imported, or compiled.

This is a private bounded working proof, subject to full saved-source
review. It does not prove the existence of a bad cancellation candidate,
exclude other frame-selection methods, or establish an intrinsic
fixed-point theorem. General cancellation is UNSOLVED and novelty is
UNKNOWN.
