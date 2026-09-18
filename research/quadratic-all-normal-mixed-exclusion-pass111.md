# Mixed double-plus-simple fibers are excluded without a speed-normal condition

The supplied actual nonconical quadratic frame has no closed fiber of
multiplicity profile (2,1), including where the speed normal vanishes.
The new step reconstructs the actual low-degree Artin generator without
the original linear-normal equation. This supplies exactly the algebraic
inputs of the full-image107, unit-image108 and proper-image110 exclusions.

The same reconstruction extends the whole-double second-degree dichotomy
to zero speed normal. Its proper-image alternative is not excluded.
Neither conclusion supplies an arbitrary cancellation-to-frame reduction
or global recognition of the threefold.

## 1. Scope and the hypotheses that remain necessary

Keep the supplied actual quadratic frame, canonical N, invariant plane S,
and actual good generators from
[fixed-fiber111](quadratic-fixed-fiber-low-degree-collapse-pass111.md).
At a closed base point let R=S_m, n=mR and K=Frac(R). Work in the
faithfully flat domain A_R with ker N=R. Its generic fiber is K[v], its
degree modules F_j are free of rank j+1, and
A_R=R[A1,A2,c], with A1,A2 in F2 and c in F4.

One retained global hypothesis is particularly important: the selected
good generators do not both become algebraic constants on any invariant
divisor. With the actual polynomial divisor fibers and primitive action91,
this gives the exact degree-one slice or degree-two conic at every
height-one prime of R. Hence
\[
\begin{gathered}
(A_R)_{\mathfrak p}=R_{\mathfrak p}[(F_2)_{\mathfrak p}],
\qquad (I_1)_{\mathfrak p}=(I_2)_{\mathfrak p},\\
I_j=N^jF_j,\qquad
\operatorname{ord}_{\mathfrak p}I_j
 =\lceil j/2\rceil\operatorname{ord}_{\mathfrak p}I_1,\\
\operatorname{ord}_{\mathfrak p}\Delta(E_4)
 =-4\operatorname{ord}_{\mathfrak p}P,\qquad I_1=PR.
\end{gathered}
\tag{1}
\]
Here E4 is any actual R-basis of F4 and its determinant is expressed in
1,r,r squared,r cubed,r fourth, where F1=R{1,r}, Nr=P.
At a degree-one divisor P is a unit, so the displayed image valuations
are all zero. At a quadratic divisor the alternating basis107 proves
them. These statements concern all base divisors, not just a chosen
closed fiber or the fourth derivative of c.[^divisor]

No condition on L(m) is imposed. No equality
nA_R=(F,G squared(G-1)) or stability of the whole ideal under the
original partial derivative is assumed or needed below.

## 2. Constructing the whole mixed Artin algebra in degree two

Suppose the whole fiber has profile (2,1). Its double component is fixed
and collapsed by the retained no-companion result96, or equivalently
the noncollapsed cyclic conclusion103. The invariant identity111 then
collapses its simple companion. The components are disjoint, and
fixed-fiber111 gives the actual factor decomposition and N-action
\[
\mathcal A=A_R/\mathfrak nA_R
 =\mathbb C[c,\epsilon]/(\epsilon^2)\times\mathbb C[c],
\qquad
\bar N=(\lambda\epsilon\partial_c,\rho\partial_c),
\qquad\lambda,\rho\in\mathbb C^*.
\tag{2}
\]
Both c's in this formula are the same specified element, projected to
the two factors.

By the [nilpotent-rank theorem111](quadratic-double-nilpotent-rank-pass111.md),
the good restrictions have the form
Ai=(alpha_i+nu_i epsilon,beta_i), with alpha_i,nu_i,beta_i in C
and nu=(nu1,nu2) nonzero. Also delta=beta-alpha is nonzero.
Otherwise A1,A2,c would generate only the diagonal C[c] on the two
reduced factors, contrary to actual generation of the whole fiber.
Choose a constant row ell with ell nu and ell delta both nonzero.
After a constant shift and division by ell delta its good combination G
has double restriction a nonzero multiple of epsilon and simple
restriction one. Scale epsilon to that double restriction. Thus
\[
\begin{gathered}
G\in F_2,\qquad \bar G=(\epsilon,1),\qquad
D=\mathbb C[\bar G]\simeq\mathbb C[G]/(G^2(G-1)),\\
\boxed{\quad
\mathcal A=D[c],\qquad
\bar N=\bigl(\lambda'(G-G^2)+\rho G^2\bigr)\partial_c,\qquad
\lambda',\rho\in\mathbb C^* .
\quad}
\end{gathered}
\tag{3}
\]
Indeed G squared projects to (0,1) and G-G squared to (epsilon,0).
These elements and 1 give the entire three-dimensional Artin coefficient
algebra. The action on D is zero. G is an actual constant good
combination, not an abstract symbol newly placed in F2.

## 3. All degree-two residues are Artin-valued

Let U be any element of F2. If its restriction to the reduced double
line is nonconstant, (2) makes NU nonzero in the generic Artinian
double fiber. The general cyclic theorem103 then provides bases of every
Fj from U and NU and identifies the entire localized algebra with its
monic conic. Its entire reduced closed fiber is a single line, contrary
to the simple companion. Thus the double reduction of U is constant.

The nilpotent-rank theorem, applied with the actual G from (3), now makes
U's nilpotent coefficient on the double constant too. On the simple
component, fixed-fiber111 makes every F2 restriction constant. Therefore,
writing Wj for the image of Fj in the whole nonreduced fiber,
\[
\boxed{\quad
\mathbb C\{1,G\}\subseteq W_2\subseteq D,\qquad
\dim W_2\in\{2,3\}.
\quad}
\tag{4}
\]
This argument replaces the old104 image proof where that proof used
the original nonzero-normal chart. Its conclusion is now derived from
the new actual data, not transferred by dropping a premise.

## 4. The full-image exclusion uses only these rebuilt data

If W2=D, choose an actual basis 1,z,w whose residues are a basis of D.
The conic matrix and (1) yield
F1=R{1,r}, r=az+bw, Nr=P, a primitive proper pair a,b,
Nz=e b r+B1, Nw=-e a r+B2, and e a unit.
The pair is proper because N kills the independent whole residues:
its zero residue matrix forces a squared and b squared into n.
Purity of the residue-independent basis puts B1,B2,Q into J squared,
where J=(a,b), Q=e r squared-2B2z+2B1w.

These are precisely the inputs of
[full-Artin quartic107](mixed-full-artin-quartic-exclusion-pass107.md),
Sections 2--4. To make the transfer explicit, that proof divides the
three quadratic coefficient polynomials of the conic by the regular
sequence a,b to obtain actual quartics U4,V4. Their combination
T=-(bU4-aV4)/2 has N cubed T=3e squared P squared, which proves
I3=P squared R. The all-height-one valuations (1) and the two relations
among U4,V4,T give a unit determinant on F4/F2. Hence
F4=R{1,z,w,U4,V4}.

The same proof establishes the exact, base-torsion-free three-relation
presentation of R[z,w,U4,V4]. Its raw closed fiber is
D[U4,V4] and has dimension two. The torsion-free step uses regular
sequences, the actual divisor presentations, and the expected
codimension of those three relations; it does not follow merely from
a generic presentation. But A_R=R[F4] by the specified A1,A2,c, so its
fiber would have dimension two instead of the dimension one in (3).
Thus W2 is not D.

Every input used in that proof has been supplied above or in (1).
There is no selected-c valuation or separate assumption that I4 is
nonprincipal. The proof produces its own cubic generator and quartic
basis. Its old L(m) condition supplied fiber data that are now obtained
in (2)--(3), and has no further use in the algebraic argument.

## 5. The rank-two alternatives are both impossible

We now have W2=C{1,G}. Necessarily W1=C: otherwise a first-degree
element with nonconstant residue A+B G, B nonzero, would give three
independent residues 1,r,r squared in W2. Independence follows because
the minimal polynomial of G has degree three.

Choose F2=R{1,G,H} with H of zero whole residue and write a centered
first-degree generator r=aG+bH. The conic matrix and (1) give
\[
\begin{gathered}
F_1=R\{1,r\},\quad Nr=P,\quad I_2=PJ,\quad J=(a,b),\quad
\gcd(a,b)=1,\\
NG=e b r+h,\qquad NH=-e a r+B_2,\qquad e\in R^*,\qquad
Q=e r^2-2B_2G+2hH\in R.
\end{gathered}
\tag{5}
\]

If J=R, the unit-image argument108 applies. More explicitly choose Y
with N squared Y=P; then 1,r,Y is a basis of F2. The coefficient of Y
in G must be a unit, since W1=C and G has nonconstant residue.
Thus r'=NG and G give a monic conic basis of F2, with
N r'=P' a unit multiple of P. The algebra R[r',G] has the free monic
basis G^j,r'G^j and agrees with A_R at every height-one prime by (1).
Its finite coefficient expansions intersect back to R in the UFD,
proving R[r',G]=A_R. Its free basis element r' must have nonzero
closed residue. This contradicts Nbar(G)=0 in (3).[^unit]

If J is proper, both a,b lie in n and are nonzero. Since H belongs
to nA_R and the piece R{1,G,G squared} has independent whole residues,
the sharp coefficient proof108 gives
\[
\begin{gathered}
a^2,B_2,Q\in\mathfrak n(h)+\mathfrak n(ab)+\mathfrak n^2(b^2),
\qquad h\in\mathfrak n\setminus\{0\},\quad \gcd(h,b)=1,\\
M=R\{1,G,G^2,GH,W\}\subseteq F_4,\qquad bF_4\subseteq M,\\
N(M)\subseteq\bigl((h)+\mathfrak n(a)+\mathfrak n^2(b)\bigr)A_R
\quad\Longrightarrow\quad
b\in(h)+\mathfrak n(a).
\end{gathered}
\tag{6}
\]
For clarity, the latter two lines are the actual divided-quartic and
index argument110, not conclusions from the sharp ideal alone. Its
division uses coprimality of h,b and flatness. Its five-column
determinant is -e fourth b/(8P fourth); (1) gives index (b), so the
adjugate gives bF4 contained in M. Differentiating its explicit W puts
N(M) in the displayed ideal. Since c is in F4 and Nc has nonzero
whole residue by (3), one-element purity contracts bNc and proves
the last membership. Alternatively Nc is a unit at every point of
the simple component, where a local faithfully flat contraction
gives the same membership.

Modulo h, write b=a v with v in the maximal ideal. The first line of
(6) now forces a squared into the maximal-ideal square times
(a squared). Nakayama gives h dividing a squared. But any common prime
factor of h,a would divide b by the last line of (6), contradicting
gcd(a,b)=1. A nonzero nonunit h cannot both divide a squared and be
coprime to a in this UFD. This is the contradiction110.[^proper]

Its only geometric uses were the actual residue-independent three-term
piece, the exact divisor determinants, and the nonzero residue of Nc.
All have been reestablished without L(m) nonzero. The two alternatives
exhaust (5), completing the mixed exclusion.

## 6. The whole-double dichotomy also loses its speed-normal premise

Suppose instead that the collapsed fixed double is the entire fiber.
Fixed-fiber111 and nilpotent-rank111 give
Abar=C[c,epsilon]/epsilon squared, Nbar=lambda epsilon partial_c,
and an actual G in F2 with Gbar=epsilon, without any L assumption.

If some U in F2 has nonconstant reduced restriction, Nbar U is
generically nonzero, so cyclic103 gives the entire conic
A_R=R[U,r], r=NU, p=Nr, with r squared-2pU+eta=0.
If no such U exists, nilpotent-rank111 makes every F2 residue lie
in C+C G. This replaces the special weighted chart in Section 3 of
the [whole-double dichotomy111](whole-double-second-degree-dichotomy-pass111.md).

The unit-I2 proof in Section 4 of that note uses only (1), the free
monic basis, and its finite coefficient intersection. If I2=I1=PR,
it proves A_R=R[U,NU], with U in F2 and N squared U=P. The
fixed-point invariant identity gives P,eta in n. The resulting
whole conic fiber has U as a reduced parameter. Thus
\[
\boxed{\begin{aligned}
&\exists U\in F_2\text{ with nonconstant reduced restriction}\\
&\quad\Longleftrightarrow I_2=I_1
\Longleftrightarrow \dim W_2=3
\Longleftrightarrow \dim W_1=2.
\end{aligned}}
\tag{7}
\]
In the other alternative, the same coprime-row argument gives
W1=C, W2=C{1,G}, I1=PR, I2=P(a,b), with (a,b) proper n-primary,
P in n squared and I2 contained in n cubed. The order proof uses
only purity of 1,G, the conic and Hbar=0; it does not extract a
coefficient of G squared.

The stronger original ideal equality in the old whole-double setting
is not part of this extension. Nor does (7) rule out its proper
alternative. G squared is zero on this whole fiber, so the sharp
mixed three-term extraction that drove (6) is unavailable.

## Verification and limits

The new geometric work is in fixed-fiber111 and nilpotent-rank111;
Sections 2--3 above connect it to the actual hypotheses needed by the
retained exclusions. The algebraic transfers were separately
reconstructed from the full saved107/108/110 proofs. They are not
inferences from test outcomes or from an unproved ideal normalization.
The specific all-L conclusions are new relative to the frozen notes,
not asserted to be new in the literature.

The [intrinsic coordinate control111](whole-double-good-coordinate-control-pass111.md)
is useful for the remaining boundary. It has a hidden quadratic parameter
even with a specified quartic c, but its selected good pair fails the
whole-divisor noncollapse input of (1). It is not an actual frame
counterexample. Formal identity checks do not certify that input.

The general complex-threefold cancellation target is unchanged and
unsolved. Whole-double recognition, its proper-image alternative,
other original-frame branches and an entry theorem for arbitrary sliced
actions remain separate obligations. No human review, Lean verification,
public outreach or novelty clearance is claimed.

[^divisor]: [Actual divisor91](nonconical-residue-degree-bound-pass91.md); [exact quadratic divisor107](quadratic-constant-divisor-filtration-pass107.md), Sections 1--5; [degree-one slice105](mixed-cubic-rank-defect-pass105.md), Section 2. The finite-free theorem is [module102](quadratic-degree-module-fiber-rigidity-pass102.md), Section 2.

[^unit]: [Unit second-image exclusion108](mixed-unit-second-image-exclusion-pass108.md), Sections 2--5. The proof needs neither a selected fourth-image generator nor a smooth conic fiber.

[^proper]: [Sharp purity restrictions108](mixed-proper-second-image-jets-pass108.md), Sections 1--3, and [proper-image exclusion110](mixed-proper-image-exclusion-pass110.md), Sections 2--4. The finite-piece purity statement is [purity107](residue-basis-purity-pass107.md), with its [Lazard theorem](https://stacks.math.columbia.edu/tag/058G) and [finite-factorization](https://stacks.math.columbia.edu/tag/058C) sources. The contraction may instead use the simple-point faithful-flat argument as stated above.
