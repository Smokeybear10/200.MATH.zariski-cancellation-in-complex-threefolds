# Cylinder actions, degree-one pencils and a nodal exhaustion obstruction

The unrestricted complex threefold cancellation conjecture remains
unproved. Three narrower arguments sharpen the current research routes.
A rank-three unipotent action on a cylinder would supply two independent
actions on its base. Every degree-one horizontal in the fixed canonical
polynomial model admits a simultaneous triangular description over
\(\mathbb C(x)\). The proposed nodal realization cannot have a simple
plinth factor, regardless of how many later modifications are allowed.

None of these results supplies the missing implication for every
polynomial cylinder. Their exact assumptions, proofs and limits are
separated below. Novelty, human expert review and proof-assistant
verification are not claimed.

## 1. The original question

The working interpretation of the professor's message is
\[
A[s]\simeq\mathbb C^{[4]}
\quad\Longrightarrow\quad A\simeq\mathbb C^{[3]}.
\tag{1}
\]
Here \(A\) is the coordinate ring of an affine complex threefold and
\(s\) is an indeterminate over it. The professor has not confirmed
either the dimensional correction to the pasted statement or this field.
The original conclusion \(X\simeq\mathbb A^1\) cannot hold for
\(r>1\), simply by dimension.

A locally nilpotent derivation, abbreviated LND, represents an algebraic
additive-group action. A slice for \(D\) is an element \(s\) with
\(D(s)=1\); the slice theorem identifies its ring with
\((\ker D)[s]\). Thus (1) asks whether the invariant ring of every
sliced action on \(\mathbb C^{[4]}\) is a polynomial ring in three
variables. A calculation for selected actions does not settle that
universal quantifier.

## 2. A sufficient group action, with its existence still open

**Proposition.** Let \(A\) be an affine complex domain of dimension
three. Suppose a connected unipotent algebraic group acts on
\(\operatorname{Spec}(A[s])\), contains the slice translation
\(E=\partial_s\), and has generic orbit dimension three. Then \(A\)
has two commuting LNDs independent over \(\operatorname{Frac}A\).

This statement does not require \(A[s]\) to be polynomial. Its
application to cancellation does require the additional group-action
hypothesis, which has not been derived from (1).

Brion's homogeneous-space theorem gives a stable product open with
affine three-space fibers and orbit quotient. A nonzero invariant in
the boundary ideal cuts out a principal product open. Such an invariant
exists because a nonzero finite-dimensional representation of a
unipotent group has a fixed vector. Consequently, for some invariant
\(h\ne0\) and an affine domain \(R\),
\[
(A[s])_h=R^{[3]},\qquad R=((A[s])^G)_h.
\tag{2}
\]
Because the group contains \(E\), its invariants and \(h\) lie in
\(A\). This is an actual principal-open equality, not merely a
birational product or an assumed finitely generated global quotient.[^1]

For \(K=\operatorname{Frac}R\), equation (2) becomes
\[
(A_h\otimes_R K)[s]=K^{[3]}.
\tag{3}
\]
Affine-plane cancellation over an algebraic closure, followed by
Kambayashi's separable affine-plane descent, gives
\(A_h\otimes_R K=K[u,v]\). These are dimension-two inputs, not
an application of the original dimension-three conjecture.[^2][^3]

The derivations \(\partial_u,\partial_v\) kill \(K\). Multiplying
them by a common invariant denominator first makes them preserve
\(A_h\), then a common power of \(h\) makes them preserve \(A\).
Those multipliers are killed by both fields, so local nilpotence,
commutation and generic independence survive. This proves the proposition.
The complete argument is in the
[rank-one cylinder note](research/rank-one-cylinder-pass35.md).

For a putative intrinsic-rank-one factor, the earlier deductions give
\(\operatorname{LND}(A)=CD\), with \(C=\ker D=\operatorname{ML}(A)\).
There is a valid relative transfer:
\[
\{L\in\operatorname{LND}(A[s]):L(s)=0\}=C[s]D.
\tag{4}
\]
Specializing at every scalar \(s\), followed by polynomial
interpolation and primitive saturation, proves (4). It gives no control
over ambient coordinate translations that move \(s\).

In particular, a rank-one candidate cannot admit a finite-dimensional
all-LND Lie algebra containing \(E\) and having generic rank at least
three. Rank three is excluded by the proposition; rank four by the
earlier transitive recognition argument. A transverse ambient partial
exists, but its Lie closure need not be finite-dimensional or all-LND.
Proving those extra properties remains a substantive missing step.

## 3. The complete degree-one sector of the fixed model

The separate canonical model is
\[
B=\mathbb C[x,\lambda,w,z],\qquad
\Delta=x^2\partial_w+2(1+\lambda x)^2w\partial_z.
\tag{5}
\]
Consider every LND \(\delta\) of this ring satisfying
\(\delta x=0\), \(\delta\lambda=1\), and
\([\delta,[\delta,\Delta]]=0\), with
\([\delta,\Delta]\ne0\). These are all degree-one horizontals
in the stated model, not just a preselected triangular family.

Since \(\lambda\) is already an ambient coordinate, the canonical
slice identification gives actual coordinates \((x,\lambda,b,c)\)
with \(\delta=\partial_\lambda\) and
\[
\Delta=D_0+\lambda D_1,\qquad
D_0=x^2\partial_b+2b\partial_c.
\tag{6}
\]
Over \(K=\mathbb C(x)\), set \(u=b/x^2\) and
\(v=x^2c-b^2\). Then \(D_0=\partial_u\). The pencil has a
slice over the entire ring \(K[\lambda,u,v]\), inherited from
the actual coordinate map. In particular its two coefficients generate
the unit ideal.

The planar LND coordinate theorem writes the nonzero top as
\(D_1=g(F)J_F\), with \(F\) a genuine coordinate of \(K[u,v]\).
This input is valid over \(K\), not only over an algebraically closed
field.[^4] Use the convention \(J_F=F_v\partial_u-F_u\partial_v\). The unit
coefficient ideal of the pencil is
\[
(\lambda gF_u,\ 1+\lambda gF_v)=K[\lambda,u,v].
\tag{7}
\]
Modulo \(gF_u\), a polynomial \(1+\lambda gF_v\) can be a unit
only when \(gF_v\) is nilpotent. Thus every irreducible factor of
\(F_u\) divides \(g(F)\), since the coordinate derivatives
\(F_u,F_v\) are relatively prime.

The case \(F_u=0\) would make the second generator in (7) a
nonconstant nonunit polynomial in \(\lambda\), and is impossible.
For \(F_u\ne0\), a nonconstant factor \(q(F)\) has \(u\)-degree
at least \(\deg_uF\), whereas \(F_u\) has smaller degree.
Irreducibles in \(K[F]\) remain irreducible in the coordinate ring
\(K[F,G]\). Therefore \(F_u\) is a nonzero constant in \(K\).
Rescaling and absorbing the scalar into \(g\) gives
\[
F=u+Q(v),\qquad
D_0=\partial_F,\qquad D_1=-g(F)\partial_v.
\tag{8}
\]
This is a simultaneous triangular description of the whole pencil.
The universal argument uses the entire unit coefficient ideal, not
finite testing of scalar parameters.

There is a further consequence. Put
\(V_j=-g^{(j)}(F)\partial_v\), for
\(0\le j\le\deg_F g\). Then
\[
[\delta,\Delta]=V_0,\quad
[\Delta,V_j]=V_{j+1},\quad
[\delta,V_j]=[V_i,V_j]=0,
\tag{9}
\]
where the next derivative is zero beyond the polynomial degree.
Although the convenient coordinates use \(\mathbb C(x)\), each
\(V_j\) is an actual iterated bracket of polynomial fields. They
therefore preserve the original ring. Their finite complex span with
\(\delta,\Delta\) is nilpotent, and every member is locally
nilpotent by (8). Its generic rank is three.

There is also a polynomial conclusion before inverting \(x\).
Divide \(D_1\) by its coefficient gcd to obtain its primitive part
\(L\). Its zero divergence gives a polynomial Hamiltonian potential.
The generic normal form then makes that potential
\[
P=p(x)b+Q(x,h),\qquad h=x^2c-b^2,\qquad p\ne0.
\]
The displayed coefficients are genuinely polynomial. A pole at
\(x=\alpha\ne0\) cannot cancel because \(b,h\) remain independent
coordinates there. At zero a leading pole would require
\(p_0b+Q_0(-b^2)=0\), whose odd and even parts force both leading
coefficients to vanish. Thus no coefficient pole survives.

Primitivity also ensures that \(P\) is nonconstant on every
\(x\)-fiber. The same highest-pole argument contracts the generic
kernel to \(\ker L=\mathbb C[x,P]\). In particular
\[
D_0P=x^2p(x),\qquad D_1P=0.
\]
This gives a common polynomial local slice for every horizontal in the
sector. It does not make \(p\) a unit or give \(P\) a polynomial
coordinate companion over \(\mathbb C[x]\).

Finally, reduction modulo \(x\) forces an exact boundary form:
\[
\overline\delta=\partial_\lambda+\alpha\partial_w+
K_\lambda(\lambda,w-\alpha\lambda)\partial_z,
\quad \alpha\in\mathbb C,\quad K(0,w)=0.
\]
Indeed the transformed Hamiltonian reduces to \(-W^2\), and its
two partial derivatives have \(\lambda\)-degree at most one.
Since \(W_b|_{\lambda=0}=1\), degree additivity forces
\(W=b+\alpha\lambda\); its leading coefficient must be constant.
Jacobian one then determines the second coordinate as a vertical
shear. This is a necessity theorem, not a lifting theorem.
The full all-degree arguments and exact scope are in the
[degree-one structure note](research/general-q1-repair-pass35.md).

This conclusion is consistent with Section 2 but does not solve (1):
the present model's slice quotient is already polynomial. The missing
step is not recognizing these supplied degree-one pairs, but producing
equally useful structure without assuming this model. General
polynomial repair of every horizontal remains a separate question.

## 4. A restriction valid across every later modification

The fixed pinched surface from the earlier investigation has normalization
\[
B_0=\mathbb C[u,y,z]/((u-1)(u-i)z-y(y-1)),
\tag{10}
\]
with the retained three conductor pairings. Suppose it is realized as
\(R=W/(F)\) for \(W=\mathbb C^{[3]}\), and its compatible action
extends to a primitive ambient LND \(E\). These are hypotheses;
neither the embedding nor the extension has been constructed.

Put \(s=u^2\), \(d=s^2-1\). The restricted invariant image and
the full restricted kernel are different rings:
\[
S=\mathbb C+d\mathbb C[s],\qquad
T=\mathbb C+d\mathbb C[u].
\tag{11}
\]
The preceding isolation result writes the full plinth as
\(F^k\beta\), with \(\beta=\kappa+FQ\) and
\(\kappa\ne0\). Localizing at \(\beta\) removes no point or
infinitesimal neighborhood of \(R\). The localized ambient ring
remains smooth; it is not assumed to remain affine three-space.

For any minimal local slice \(r\), trace subtraction gives
\(\overline r=du\,b(s)\), with \(b\ne0\). Let \(K\) be any
ambient invariant lifting \(\overline r^{\,2}\). The new conclusion is
\[
1\le v_F(r^2-K)<k,
\qquad\text{and hence}\qquad k\ge2.
\tag{12}
\]
Differentiating the relation first proves that its order is at most
\(k\). If that order equals \(k\), the actual intermediate ring is
\[
H=C[\beta^{-1}][r,a],\qquad
F^ka-r^2+K=0,
\tag{13}
\]
where \(C=\ker E\). Its residue ring is a polynomial ring in
\(\overline a\) over \(S[\overline r]\). Indeed
\(\overline r\) has the stated irreducible quadratic minimal
polynomial over \(\mathbb C(s)\), while
\(D(\overline a)=2\kappa\overline r\ne0\) makes
\(\overline a\) transcendental over \(\mathbb C(u)\).
Thus \(H/FH\to R\) is injective.

An elementary saturation argument now controls all later rings at once.
If \(H\subset B\subset H[F^{-1}]\) and
\(H/FH\to B/FB\) is injective, choose the least denominator power
of any element of \(B\). Injectivity reduces that power unless it
is zero. Hence \(B=H\). Applying this to the whole unknown localized
ambient ring forces it to equal (13).

But (13) is singular above the node: both \(F\) and \(K\) lie
in the square of its maximal ideal, so every partial derivative
vanishes at \(r=0\) along that fiber. This contradicts smoothness
and proves (12). No restriction on the number or form of later
modifications was imposed. The full proof is in the
[nodal exhaustion note](research/isolated-node-realization-pass35.md).

For \(k\ge2\) and order strictly below \(k\), the new residue
is invariant, so the crucial transcendence and injectivity argument
no longer applies. Raising the order would require lifting further
elements of \(T\) to \(S\), which is not automatic because
\(T/S=du\mathbb C[s]\ne0\). These higher-exponent realizations
remain unresolved. The literature's polynomial-normalization theorem
does not supply the stronger contractibility statement that would
exclude the node outright.[^5]

## 5. Verification and the remaining proof obligations

The [complete saved regression](verification-pass-35.json) passes all
789 methods across 75 suites, including five new nodal-exhaustion
controls and seven new degree-one controls. The run was completed
on September 13, 2026. The [execution audit](research/proof-audits-pass35.md)
records the separate written reconstructions and the initial expression
comparison corrections. Repeated executions are not additional tests.

The source-dependent structural proofs and the finite exact controls
have different roles. Polynomial tests can catch an incorrect identity,
derivative or denominator example. They cannot establish existence of
a group action on every cylinder or classify every modification tower.
The general arguments above must be checked as written proofs.

The outstanding original obligation is to force sufficient intrinsic
recognition structure from (1). Section 2 gives a sufficient group
condition, not its existence. Section 3 verifies a whole useful sector,
but on an already polynomial model. Section 4 excludes exponent one
in an auxiliary realization problem, not all its cases and not every
possible cancellation counterexample.

These are bounded advances. They are not a complete cancellation proof
or a certified breakthrough.

## Sources

[^1]: Michel Brion, [*Homogeneous varieties under split solvable algebraic groups*](https://arxiv.org/pdf/2101.12452), v2, Theorems 1-2, Section 5.2 and Remark 5.2. Used only with a supplied connected unipotent algebraic action.

[^2]: Nikhilesh Dasgupta and Neena Gupta, [*An algebraic characterization of the affine three space*](https://arxiv.org/pdf/1709.00169), v2, Lemmas 2.2 and 2.5 and Theorem 2.6. These recalled classical inputs reconstruct the required affine-plane cancellation step over an algebraic closure.

[^3]: Amartya Kumar Dutta, Neena Gupta and Animesh Lahiri, [*On Separable A2 and A3-forms*](https://arxiv.org/pdf/1802.03777), v2, Theorem 2.8, explicitly recalling Kambayashi's theorem for separably algebraic affine-plane forms over fields.

[^4]: Shigeru Kuroda, [*The automorphism theorem and additive group actions on the affine plane*](https://arxiv.org/pdf/1604.04070), Theorem 1.1 and its complete proof, pages 1-3. The invariant-coordinate theorem over arbitrary fields is the published input; the unit-ideal pencil deduction is written separately above.

[^5]: Shulim Kaliman, [Seattle survey](https://www.math.miami.edu/~kaliman/library/seattle.paper.pdf), Section 10, Theorem 10.1 and Remarks 10.2 and 10.4. Polynomial normalization is proved; the stronger contractibility assertion is stated as a suspicion, and the simple modification description has additional hypotheses.
