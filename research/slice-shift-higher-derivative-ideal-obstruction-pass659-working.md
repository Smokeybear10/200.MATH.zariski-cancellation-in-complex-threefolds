# A finite ideal obstruction to every slice shift and linear frame

September 18, 2026. Private working consequence. Novelty: UNKNOWN.

For a supplied actual polynomial cylinder, a finite higher-derivative
ideal gives a necessary test for the unit normal condition simultaneously
over ALL polynomial slice shifts and ALL constant linear ambient frames.
The test can be computed in the ambient polynomial ring without first
computing the invariant ring. Its failure excludes those operations;
its success does not supply a graph section or commuting projected fields.
An exact normalizer calculation extends the exclusion to nonlinear
ambient frame changes that preserve the SUPPLIED embedded invariant
algebra A. Arbitrary nonlinear frame changes are not covered.

The ideal must retain its nonreduced structure. The retained curvature
control22 fails the test modulo a square, while reduction to the radical
loses the obstruction. This is a limitation of a specified repair route,
not a cancellation counterexample.

## 1. Actual input and all slice shifts

Let k be a field of characteristic zero and fix
\[
B=k[X_0,\ldots,X_n]=A[u],\qquad n\ge1,\qquad
E\in\operatorname{LND}_k(B),\quad E(u)=1,\quad A=\ker E.
\tag{1}
\]
The displayed equality is an actual product. Let rho:B to A be
evaluation at u=0. Every other slice for this SAME E is uniquely
v=u+h with h in A, since E(v-u)=0. Its projection is
\[
\rho_h(F)=F|_{u=-h}=\rho\bigl(\exp(-hE)F\bigr).
\tag{2}
\]
Here hE is an LND because E(h)=0. This is a change of slice with
the action and ambient frame fixed, not an arbitrary new action.

Write the normal vector and its shifted versions as
\[
e_i=\rho(EX_i),\qquad e_i^h=\rho_h(EX_i).
\tag{3}
\]
These equal the principal-retraction normal coefficients used in
[654](commuting-projected-partials-retraction-recognition-pass654-working.md)
and [656](three-commuting-projected-partials-unit-normal-recognition-pass656-working.md).
Indeed the coefficient of v in X_i expanded in A[v] is rho_h(EX_i).
The unit normal condition after a constant linear frame change is
the existence of constants lambda_i with sum lambda_i e_i^h=1.
A nonzero constant value other than one can be rescaled to one.

## 2. The higher-derivative ideal descends to the base

Define the ambient ideal
\[
J=\bigl(E^jX_i:\ 0\le i\le n,\ j\ge2\bigr)B.
\tag{4}
\]
Only finitely many generators are nonzero, by local nilpotence.
The ideal is E-stable: differentiating a generator gives another
generator, and the Leibniz rule handles its polynomial multiples.

We use the following elementary fact. Every E-stable ideal L of
A[u], with E=partial_u, is extended from A. For F in L, its finite
Taylor projection satisfies
\[
\rho(F)=\sum_{r\ge0}\frac{(-u)^r}{r!}E^rF\in L.
\tag{5}
\]
The coefficient of u^r in F is rho(E^rF)/r!, and therefore belongs
to L intersection A. Every coefficient lies in that intersection,
so L=(L intersection A)B. This proof uses inverses of factorials,
which are available because k is a characteristic-zero FIELD.

In particular, with I=J intersection A,
\[
J=IB,\qquad I=\rho(J)
 =\bigl(\rho(E^jX_i):j\ge2,\ 0\le i\le n\bigr)A.
\tag{6}
\]
For the last equality, apply the surjective algebra map rho to the
finite generating ideal (4). The ideal I is equivalently generated
by all positive-u coefficients of all EX_i, or by all u-coefficients
of all E^2X_i. The nonzero factorial factors do not change the ideal.

Both J and I are unchanged when the slice u is replaced by u+h:
J was defined without choosing a slice, and I=J intersection ker E.
They are also unchanged by any constant invertible affine frame
change Y=S X+d. In fact E^jY=S E^jX for j>=2, and S is invertible.
No invariance under arbitrary nonlinear ambient changes is asserted.

## 3. A uniform necessary test computed entirely in B

Finite Taylor expansion gives
\[
e_i^h=e_i+\sum_{r\ge1}\frac{(-h)^r}{r!}\rho(E^{r+1}X_i)
\equiv e_i\pmod I,
\qquad EX_i\equiv e_i\pmod J.
\tag{7}
\]
Consequently a unit constant projected normal at ANY shifted slice
requires
\[
1\in\operatorname{span}_k\{\overline e_0,\ldots,\overline e_n\}
\subseteq A/I.
\tag{8}
\]
Equivalently, there must be constants lambda_i such that
\[
\sum_i\lambda_i EX_i-1\in J.
\tag{9}
\]
To see the equivalence, use (7) and J intersection A=I. This does
not require solving for h, or selecting coordinates of A.

Over an exact computable coefficient field, compute a Groebner basis
of J in the given ambient polynomial ring. The reduced normal-form
map is k-linear, so (9) is the finite linear equation
\[
\sum_i\lambda_i\operatorname{NF}_J(EX_i)
 =\operatorname{NF}_J(1).
\tag{10}
\]
Compare the finitely many ambient monomial coefficients. The supplied
polynomial derivation E computes every generator of J by iteration;
the local-nilpotence hypothesis ensures termination on each X_i.
This calculation needs neither generators nor defining equations for A.
An exact coefficient-equality and Groebner-computation oracle also
suffices. No algorithm is claimed for arbitrary unrepresented complex
constants.

If J is proper, a solution of (9) is automatically nonzero. If J=B,
then I=A and (8)--(10) are vacuous: even lambda=0 satisfies (9).
This case provides no direction, slice shift, or recognition result.
The case J=0 is allowed too; then all EX_i lie in A, and the normal
condition itself is independent of the chosen slice.

Inconsistency of (10) excludes the criterion656 for EVERY h in A and
EVERY constant linear ambient frame. Consistency is only necessary.
Even an actual unit normal still needs the complementary commutation
condition of656, or equivalently the full fixed-slice system of
[657](constant-linear-frame-projected-commutation-test-pass657-working.md).

## 4. What a unit normal means geometrically

For fixed constants lambda_i put ell=sum lambda_i X_i. For a fixed
h in A the following conditions are equivalent:
\[
\rho_h(E\ell)=1;\qquad E\ell-1\in(u+h)B;\qquad
\ell=r+(u+h)+(u+h)^2Q
\quad\text{for some }r\in A,\ Q\in B.
\tag{11}
\]
The first two conditions use ker rho_h=(u+h)B. For the last, expand
ell in A[v], v=u+h. The first condition says exactly that its
coefficient of v is one; its constant coefficient is r=rho_h(ell).
Conversely differentiating the last expression and setting v=0
gives the first condition.

Equivalently, the closed subscheme V(E ell-1) inside Spec A[u] admits
the graph section u=-h of its projection to Spec A. Every regular
section over Spec A is such a graph, since an A-algebra homomorphism
A[u] to A is determined by the image of u. This is a section of
that projection, not the claim E ell=1 in all of B.
Condition (9) is a necessary quotient test for existence of such a
section. It does not construct one.

## 5. The exact shifted commutator formula

Let T_i=partial_{X_i}, and use the product (1) to write uniquely
\[
T_i=P_i(u)+q_i(u)E,\qquad
P_i(u)=\sum_r u^rP_{ir},\quad P_{ir}\in\operatorname{Der}_k(A),
\quad q_i(u)=T_i(u)\in A[u].
\tag{12}
\]
There are finitely many coefficient derivations: for each T_i take
a u-degree bound on its values on the finite generating list rho(X_j),
and compare coefficients in the derivation rule. Define
\[
D_i^h=P_i(-h),\qquad K_i^h=P_i'(-h),\qquad
\nu_i^h=q_i(-h)+D_i^h(h)=\rho_h\bigl(T_i(u+h)\bigr).
\tag{13}
\]
The prime differentiates the formal u parameter while fixing A.
Since the whole ambient partials commute, their horizontal bracket
identity is [P_i,P_j]+q_iP_j'-q_jP_i'=0. But differentiating the
substituted coefficients of P_j(-h) introduces derivatives of h.
For every a in A, the polynomial chain rule gives
\[
[D_i^h,D_j^h](a)
 =\rho_h([P_i,P_j](a))
  -D_i^h(h)K_j^h(a)+D_j^h(h)K_i^h(a).
\]
Therefore the exact whole identity is
\[
[D_i^h,D_j^h]=\nu_j^hK_i^h-\nu_i^hK_j^h.
\tag{14}
\]
It is generally incorrect to substitute u=-h into an unshifted
projected bracket and omit these chain-rule terms. Formula (14)
reduces to the retained defect formula23 when h=0.

For any FIXED h, equations657 apply with e^h and the brackets (14).
When h is unknown they give polynomial equations involving h and its
first derivatives under coefficient derivations on A. No uniform
degree bound or algorithm deciding those unknown-h equations is
proved here. Furthermore D_i^h need not preserve I. Nothing above
asserts that these projected derivations or their brackets descend
to A/I; the quotient test in Section3 concerns only the normal vector.

## 6. Exact extension to frame changes preserving the embedded base

Suppose sigma is a polynomial automorphism of B with sigma(A)=A,
and write alpha=sigma|_A. Extend alpha coefficientwise to A[u],
fixing u. Then alpha^(-1) sigma is an A-algebra automorphism of
A[u]. It and its inverse have positive u-degrees whose product is
one, so both are linear in u. Their leading coefficients are units
of A, which are exactly k*. Therefore
\[
\sigma(u)=cu+h,\quad c\in k^*,\ h\in A,\qquad
E\sigma=c\sigma E,\qquad \sigma E\sigma^{-1}=c^{-1}E.
\tag{15}
\]
Conversely the last equality implies sigma(A)=A by taking kernels.
Thus preserving the embedded base is exactly normalizing the line kE.

Put f=-alpha^(-1)(h). Checking on A and u proves the whole identity
\[
\rho\sigma=\alpha\rho_f.
\tag{16}
\]
For the new ambient frame sigma(X_i), its actual coordinate partial
is sigma T_i sigma^(-1). Its projected normal and projected fields
at the original slice consequently satisfy
\[
e_i^\sigma=\rho(E\sigma X_i)=c\alpha(e_i^f),\qquad
D_i^\sigma=\rho\sigma T_i\sigma^{-1}|_A
 =\alpha D_i^f\alpha^{-1}.
\tag{17}
\]
This calculation allows an arbitrary residual automorphism alpha;
it does not assume that sigma fixes A pointwise. Constants are fixed
by alpha. Thus a constant normal combination for the sigma-frame
corresponds to one for the f-shift after rescaling its coefficients
by c. Commutation and the A-basis property of the complementary
projected fields are preserved by the conjugation in (17).

Conversely sigma_f=exp(-fE) fixes A and sends u to u-f, so every
shifted system occurs in this manner. Constant linear coordinate
changes commute with applying the k-algebra map sigma to a coordinate
list. Hence, allowing all constant linear frames on both sides,
existence of a frame meeting656 after a slice shift is equivalent
to existence after an ambient automorphism preserving this embedded A.

In particular inconsistency of (10) excludes this entire normalizer
route as well. It does not exclude nonlinear coordinate changes
moving the embedded subalgebra A. Nor is literal invariance of the
old ideal J under every such nonlinear automorphism being asserted;
the conclusion follows from the exact correspondence (17).

## 7. The retained curvature control excludes all shifts

In B=k[x,y,z,t], use the actual sliced action and coordinates from22:
\[
E=y\partial_x+(1+2xy)\partial_t,\quad
u=t-x^2,\quad a=x-yu,\quad b=y,\quad c=z.
\tag{18}
\]
The complete inverse is
x=a+bu, y=b, z=c, t=u+(a+bu)^2. Thus E=partial_u and
A=k[a,b,c]. The nonzero second coordinate derivative is E^2t=2y^2,
and every third coordinate derivative vanishes. Hence
\[
J=(y^2)B,\qquad I=(b^2)A,\qquad
e=(b,0,0,1+2ab).
\tag{19}
\]
For an ARBITRARY h in k[a,b,c], the shifted normal is exactly
\[
e^h=(b,0,0,1+2ab-2b^2h).
\tag{20}
\]
Modulo b^2, a constant normal combination equaling one would require
lambda_x b+lambda_t(1+2ab)=1. Modulo b this forces lambda_t=1;
the coefficient of b then requires lambda_x+2a=0 in k[a,c],
which is impossible. Therefore no slice shift and no constant affine
ambient frame can meet the unit-normal condition. In particular none
can meet656. No finite-degree restriction on h was imposed.

The nonradical ideal matters. Modulo rad(I)=(b), the normal vector
is (0,0,0,1), so the reduced-ideal test would pass. The same action
has the explicit nonlinear coordinate frame (a,b,c,u). Thus the
obstruction is not invariant under all nonlinear frame changes and
does not prevent actual recognition.

For clarity, the shifted projected fields in the original order are
\[
D_x^h=(1+2ab-2b^2h)\partial_a,\quad
D_y^h=h\partial_a+\partial_b,\quad
D_z^h=\partial_c,\quad D_t^h=-b\partial_a.
\tag{21}
\]
Here K_x^h=2b^2 partial_a, K_y^h=-partial_a, and K_z^h=K_t^h=0.
In particular
\[
[D_y^h,D_t^h]=(b\partial_a h-1)\partial_a,
\tag{22}
\]
whereas the unshifted bracket was simply -partial_a. This verifies
the need for the derivative-of-h terms in (14). Also D_y^h(b^2)=2b,
so I is not preserved, as warned above.

## 8. Deduplication and proof scope

The exact unshifted bracket defect and variable-time descent boundary
are retained in [23](leading-derivation-pass23.md), Sections2--3.
The slice projections and their dependence on the selected slice
are retained in [74](quadratic-slice-projection-pass74.md).
The actual curvature control and its full inverse are from
[22](nonlinear-frame-pass22.md), not a new construction.
The [quadratic-time control124](quasi-nice-full-acceleration-span-pass124.md)
already uses the term acceleration ideal for a special frame where
that ideal is the unit ideal. It does not state the all-shifts
quotient-normal test proved here. The bounded archive search found
no identical retained uniform test; no literature novelty is inferred.

Root and the author independently reconstructed the ideal obstruction
and shifted-bracket proof. Root supplied the ambient-only normal-form
implementation in (9)--(10); Geometry supplied the normalizer
correspondence (15)--(17), independently reconstructed here. All
results here are written algebraic arguments; fresh unsaved exact
algebra is used only to check the printed control identities.
No saved checker was executed, imported,
compiled, or changed. No canonical file was edited.

Root, General, and Geometry read the complete held source and
independently reconstructed the proof. Both separate reviewers
reported CLEAN, including the nonidentity residual automorphism
and scaling in Section6. Reviewed hashes and full-read evidence
are recorded in the ledger. These are internal AI checks, not
human expert review or formal proof certification.

Neither failure nor consistency of this necessary test settles the
general existence of useful nonlinear coordinates. General
cancellation remains UNSOLVED and novelty UNKNOWN.
