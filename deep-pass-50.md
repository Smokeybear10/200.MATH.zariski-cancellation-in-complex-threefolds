# Multi-tangent constraints and the limits of local slice repair

Two plausible repairs of the remaining quadratic obstruction have
precise limits. The trace argument gives a stronger necessary condition
when distinct tangent directions occur, but does not exclude ordinary
triple points by itself. Localizing at new low-degree fiber invariants
does not create a bounded polynomial slice that was absent before
localization. A square-root extension supplies actual local slices,
but may destroy finite intrinsic derivative degree.

The full cancellation question is still unresolved. The working
interpretation remains
\[
A[s_*]\simeq\mathbb C^{[4]}
\quad\Longrightarrow\quad A\simeq\mathbb C^{[3]}.
\tag{1}
\]
The professor has not confirmed this correction of the dimensional
inconsistency in the pasted email. No unrestricted variety is proved
here to admit the particular coordinate frame studied below.

## 1. Actual setup and the remaining obstruction

Let \(E(s_*)=1\) on the actual polynomial four-ring
\(B=A[s_*]\), and let \(D\) be the primitive intrinsic locally
nilpotent derivation of the independent degree-two branch. Put
\[
C=\ker D\simeq\mathbb C^{[2]},\quad
F_n=\ker D^{n+1},\quad
\operatorname{pl}(D)=pC,\quad I_2=D^2(F_2)=pJ.
\tag{2}
\]
The actual cylinder and the published quotient theorem supply the
affine-plane quotient and faithful flatness; this is not a theorem
about an assumed polynomial three-ring.[^1]

At a closed second-image obstruction point, set
\(R=C_{\mathfrak m}\), \(\mathfrak n=\mathfrak mR\), and
\(\mathcal A=A_R\). The inherited local relations are
\[
F_2(\mathcal A)=R\oplus Rz\oplus Rw,\qquad
r=az+bw,\qquad JR=(a,b),\qquad\gcd(a,b)=1,
\tag{3}
\]
\[
Dr=p,\quad Dz=\epsilon br+B_1,\quad
Dw=-\epsilon ar+B_2,\quad
p=aB_1+bB_2,
\tag{4}
\]
\[
\epsilon r^2-2B_2z+2B_1w-Q=0,\qquad \epsilon\in R^*.
\tag{5}
\]
All \(a,b,B_1,B_2,Q\) belong to \(\mathfrak n\).
The full normalized-cover argument and actual quadratic invariant
field identify the trace of the residue of \(r\) on every
normalized plinth branch. An arbitrary conic relation is not enough.

The [previous report](deep-pass-49.md) excludes smooth points and
ordinary nodes of the full plinth from obstruction support.
The [multi-tangent proof](research/multitangent-plinth-boundary-pass50.md)
extends the necessary condition. The
[fiber-open proof](research/fiber-invariant-opens-pass50.md)
analyzes the separate local-slice repair.

## 2. Two tangent directions force a stronger ideal membership

On a normalized branch \(\xi\), if \(b\) is nonzero on its
plinth component, the actual quadratic minimal polynomial gives
\[
\operatorname{ord}_\xi(B_1)\ge
\operatorname{ord}_\xi(b)+1.
\tag{6}
\]
If \(b\) is identically zero, coprimality and (4) make \(B_1\)
identically zero there. The companion assertion concerns \(a,B_2\).
These statements use normalized-cover surjectivity and the fact
that \(r\) vanishes on the entire actual fiber.

Suppose the branch has multiplicity \(e\). In regular plane
parameters \(u,v\), its leading parametrization has the form
\[
(u,v)=t^e(\alpha,\beta)+\text{higher terms},
\qquad (\alpha,\beta)\ne(0,0).
\tag{7}
\]
Every element of \(\mathfrak n\) has branch order at least \(e\).
Equation (6) therefore puts \(B_1\) in order at least \(e+1\),
unless it vanishes identically. Its linear part must annihilate
\((\alpha,\beta)\): otherwise the order would be exactly \(e\).
Terms of \(\mathfrak n^2\) cannot cancel that leading term.
The same argument applies to \(B_2\).

Thus if the reduced plinth support has two distinct tangent
directions at the point, even if individual branches are singular,
\[
\boxed{B_1,B_2\in\mathfrak n^2,\qquad
p\in\mathfrak n^2JR.}
\tag{8}
\]
Writing \(m=\operatorname{ord}_{\mathfrak n}(p)\), this implies
\[
\operatorname{ord}_{\mathfrak n}(J)\le m-2.
\tag{9}
\]
The full plinth, including multiplicities, occurs in \(m\).
For an ordinary node, \(m=2\) is impossible because \(J\) is
proper. At an ordinary triple point, the result only forces
a generator of \(J\) with a nonzero linear part.
It does not force \(J=R\) or \(J=\mathfrak n\).

## 3. The ordinary-triple control and its exact missing hypotheses

Consider the explicit auxiliary domain
\[
H=\mathbb C[a,b,z,w]/
\bigl((az+bw)^2-2b^2z-2a^2w+ab-a^3\bigr),
\quad r=az+bw,\quad p=b^3-a^3.
\tag{10}
\]
Set \(B_1=-a^2\), \(B_2=b^2\), \(\epsilon=1\) and
\(Q=-ab+a^3\). These coefficients satisfy the local conic
identities and (8). The base polynomial has an ordinary triple
point at the origin.

Over \(\mathbb C(a,b)\), the independent linear functions
\(r=az+bw\) and \(j=-b^2z-a^2w\) have determinant \(p\).
The equation becomes \(r^2+2j-Q=0\), an irreducible polynomial.
The original equation is primitive over \(\mathbb C[a,b]\),
so the global quotient is a domain by Gauss's lemma.

The derivation
\[
Da=Db=0,\qquad Dz=br-a^2,\qquad Dw=-ar+b^2
\tag{11}
\]
is a genuine LND on \(H\). It preserves the relation,
\(Dr=p\), \(D^2z=bp\), \(D^2w=-ap\), and both third
coordinate derivatives vanish. No polynomial-cylinder
presentation or full-plinth computation for \(H\) is asserted.

For each \(\zeta^3=1\), restrict to \(a=t,b=\zeta t\).
The dominating generic quadratic field has equation
\[
(r-\zeta^2t)^2=t^3,\qquad
t=s^2,\quad r=\zeta^2s^2+s^3.
\tag{12}
\]
The normalization is finite and birational, with inverse
\(s=(r-\zeta^2t)/t\) in the fraction field. Its cover of
the base line has one finite branch value; \(r\) vanishes
at its only point over zero, and its trace is \(2\zeta^2t\).

The dominating exceptional surface is also explicit:
\((z+\zeta w-\zeta^2)^2=t\). It is a polynomial plane
with coordinates \(s,z\), mapping surjectively to the
normalized invariant line. Its induced derivation is
\(\zeta s^5\partial_z\), so its full invariant ring is
\(\mathbb C[s]\).

However, the full branch pullback is
\[
H/(b-\zeta a)H=
\mathbb C[t,z,w]/
\bigl(t^2((z+\zeta w-\zeta^2)^2-t)\bigr).
\tag{13}
\]
It has a double vertical plane. It is not the prime reduced
exceptional surface required by the actual factorial quotient.

Flatness fails explicitly. Modulo \(b\), the defining relation is
\[
a^2(z^2-2w-a)=0.
\tag{14}
\]
The nonzero class \(a(z^2-2w-a)\) is annihilated by \(a\),
so the base regular sequence \(b,a\) is not preserved.
The total hypersurface is singular along \(a=b=0\).
Its closed fiber there is a plane, not the actual quotient curve.

Consequently this control does not contradict cancellation or
the full actual hypotheses. It proves a narrower failure:
conic identities, dominating quadratic fields, reached normalized
points, one-branch covers and trace vanishing alone cannot
exclude an ordinary triple point. Actual flatness and prime
pullbacks must enter any stronger argument.

## 4. Two low-degree invariants cover the entire exceptional fiber

Use the actual original coordinates \(x_1,\ldots,x_4\).
In the independent degree-two branch,
\[
f=Ex_3,\quad g=Ex_4,\quad h_i=E^2x_i\in C,\qquad
B_L=L[x_3,x_4],\quad A_L=L[j],\quad j=gx_3-fx_4,
\tag{15}
\]
where \(L=\operatorname{Frac}C\). The good coordinates
are quadratic polynomials in the bad pair over \(L\).
Assume \(\mathfrak m\supset(f,g,h_1,h_2)\), the remaining
locus identified in the preceding report.

Set \(A_0=A_R\), \(B_0=A_0[s_*]\), and use bars for
reduction modulo \(\mathfrak m\). Write \(P_i=Ex_i\) and
\[
I_i=P_i^2-2h_ix_i,\qquad
I_{12}=P_1P_2-h_2x_1-h_1x_2.
\tag{16}
\]
All three are actual \(E\)-invariants. The generic graph
makes them intrinsic elements of \(F_2(A_0)\).

The good velocity residues \(p_i=\overline{P_i}\) are
invariant under the reduced \(E\). The original slice identity
is \(1=\sum_\nu(\partial s_*/\partial x_\nu)Ex_\nu\).
Reduce it modulo \(\mathfrak m\) and evaluate at \(s_*=0\)
in \(\overline B=\overline A[s_*]\). The bad terms vanish,
giving
\[
(p_1,p_2)\overline A=\overline A,\qquad
(\overline I_1,\overline I_2)\overline A=\overline A.
\tag{17}
\]
The second equality follows from the first because
\(\overline I_i=p_i^2\). Cubing a Bezout identity supplies
an explicit Bezout identity for the squares.

Thus two \(F_2\) principal opens cover the whole
scheme-theoretic fiber, not only its reduced points.
The denominators are \(E\)-invariant, but need not be
\(D\)-invariant. Local nilpotence of \(D\) on those
localized rings cannot be assumed.

## 5. Moving denominators cannot supply new finite-degree elements

The actual local ring \(A_0\) is a UFD with
\((A_0)_L=L[j]\). For \(0\ne I\in A_0\), let \(c\)
be the product of its distinct \(D\)-invariant prime factors.
Then, inside the fraction field,
\[
A_0[I^{-1}]\cap L[j]=A_0[c^{-1}].
\tag{18}
\]
Indeed a prime of \(A_0\) becomes a unit over \(L\)
exactly when it divides a nonzero invariant. Additivity
of LND degree makes such a prime itself invariant.
Every other prime stays prime and nonunit in \(L[j]\),
so it cannot remain in a reduced denominator of a
polynomial in \(j\).

A rational function in \(L(j)\) killed by a power of the
nonzero constant multiple of \(\partial_j\) is a polynomial.
A finite pole persists under repeated differentiation.
Thus (18) also identifies the entire finite-\(D\)-degree
part of the localization. Degree by degree it gives
\[
\ker D^{n+1}\bigm|_{A_0[I^{-1}]}=F_n(A_0)[c^{-1}].
\tag{19}
\]

If the principal open defined by \(\overline I\) meets
the actual closed fiber, no invariant prime factor of \(I\)
can be a nonunit of \(R\). Such a factor would belong
to \(\mathfrak mR\), forcing \(\overline I=0\).
Consequently the right sides of (18) and (19) are then
\(A_0\) and \(F_n(A_0)\), respectively.

Now suppose \(\sigma\in B_0[I^{-1}]\) is an actual
\(E\)-slice, and all four projected original coordinates
have finite intrinsic degree. Write \(\sigma=s_*+b\),
with \(b\in A_0[I^{-1}]\). The bad projections satisfy
\[
\rho_{s_*}(x_3)-\rho_\sigma(x_3)=fb.
\tag{20}
\]
Both left terms have finite degree. Since \(Df=0\) and
\(f\ne0\), so does \(b\). Equation (18) contracts \(b\)
to \(A_0\), hence \(\sigma\) to \(B_0\).
The degree bounds descend unchanged.

This applies to each nonempty fiber open in (17).
Those opens do not create new bounded polynomial slices
that were unavailable in the original local ring.

## 6. A single degree-three projected list is already degree two

Choose an affine generic slice \(\sigma_0\) over \(L\),
such as \(x_3/f\). Any actual slice of \(B_0\) is
\(\sigma=\sigma_0+H(j)\), with \(H\in L[j]\).
The quadratic graph writes a good coordinate as
\[
x_i=\frac{h_i}{2}\sigma_0^2+
A_i(j)\sigma_0+B_i(j),\qquad
\deg A_i\le1,\quad \deg B_i\le2.
\tag{21}
\]
Projection along \(\sigma\) replaces \(\sigma_0\) by
\(-H\). If \(N=\deg H\ge2\) and \(h_i\ne0\),
the resulting degree is exactly \(2N\). The other
terms have degree at most \(N+1\) and two.
At least one \(h_i\) is nonzero in the genuine
degree-two case.

Therefore, for one chosen slice,
\[
\begin{split}
&\rho_\sigma(x_\nu)\in F_3\text{ for all }\nu\\
&\quad\Longleftrightarrow
\sigma\text{ is affine-linear over }L\text{ in }x_3,x_4\\
&\quad\Longleftrightarrow
\rho_\sigma(x_\nu)\in F_2\text{ for all }\nu.
\end{split}
\tag{22}
\]
Constant and zero \(H\) are included. Section 5 extends
the assertion to the nonempty localized fiber opens.

At an actual second-image basepoint, such a list would
generate all \(A_0\) by \(F_2\). The exact conic (5)
would then give its full fiber, a two-dimensional plane.
That contradicts the actual one-dimensional fiber.
Hence no single-slice \(F_3\)-bounded projected list can
provide that repair.

This does not yet exclude a different generating set
inside \(F_3\). It also does not prove that an actual
obstruction point exists. Both qualifications matter.

## 7. The square-root construction is valid but unbounded

For one good coordinate write \(X=x_i\), \(P=EX\),
\(H=E^2X\) and \(I=P^2-2HX\). After inverting \(I\),
adjoin \(\kappa^2=I\). This is finite étale: the
polynomial is monic and its derivative \(2\kappa\)
is invertible.[^2] Extend \(E\) by \(E\kappa=0\).

Using the original actual slice, write
\[
P=Hs_*+a,\quad
X=\frac H2s_*^2+a s_*+b,\quad
I=a^2-2Hb,\qquad a,b\in A_0.
\tag{23}
\]
On the invariant open \(a+\kappa\ne0\), set
\[
\sigma=s_*+\frac{2b}{a+\kappa},
\qquad E\sigma=1,\qquad H\sigma=P-\kappa.
\tag{24}
\]
No division by \(H\) is used to define this actual element.
The opposite sign works on \(a-\kappa\ne0\).
The two opens cover because \(\kappa\) is a unit.

Inverting \(P+\kappa\) directly is different:
\(E(P+\kappa)=H\). The rational formula
\(2X/(P+\kappa)\) alone does not justify a polynomial
slice theorem on that noninvariant localization.

The intrinsic derivation on the étale extension satisfies
\(D\kappa=(DI)/(2\kappa)\). It need not be locally
nilpotent there. For an actual polynomial-coordinate control,
take
\[
E=\partial_s,\quad D=\partial_a,\quad
X=a+s+\frac u2s^2,\quad
(x_1,x_2,x_3,x_4)=(X,s,u,v).
\tag{25}
\]
Its inverse is polynomial and its adjoint profile is
\((0,1,2,0)\), not the unresolved \((1,1,2,2)\).
Here \(I=1-2ua\), and (24) is
\(\sigma=s+2a/(1+\kappa)\).
For every \(n\ge1\),
\[
D^n\kappa=(-2u)^n
\prod_{j=0}^{n-1}\left(\frac12-j\right)
\kappa^{1-2n}\ne0.
\tag{26}
\]
The constructed slice and its projection of \(s\) have
infinite intrinsic degree. The ring already has the
ordinary coordinate slice \(s\). This control isolates
the failed inference from an étale normalized slice
to a bounded polynomial one.

## 8. Verification and remaining proof obligations

The [working proof audit](research/proof-audits-pass50-working.md)
records independent complete readings and checker runs.
The [topology re-audit](research/normalized-cover-adversarial-audit-pass50.md)
exposes the whole-fiber excision, proper-normalization and
peripheral-loop arguments again; it is a same-author
reconstruction, not another independent certification.[^3]

The finite controls are reproducible with:

~~~sh
/opt/anaconda3/bin/python research/multitangent_plinth_boundary_checks_pass50.py
/opt/anaconda3/bin/python research/fiber_invariant_opens_checks_pass50.py
~~~

There are three methods for the triple-conic control
and one for the actual square-root control. These do
not prove the universal tangent or denominator statements.
The latter have written proofs, separately from the
finite examples and recurrence checks.

The [captured full regression](verification-pass-50.json)
passes 984 methods in 118 suites, including these four
new methods. Its [integrity checker](research/consistency_checks_pass50.py)
checks hashes, links, registry scope and method counts,
not the universal mathematical proofs. Reproduce it with:

~~~sh
/opt/anaconda3/bin/python research/run_regression_pass50.py
/opt/anaconda3/bin/python research/consistency_checks_pass50.py
~~~

The decisive remaining task is to control the actual
higher-degree algebra, rather than only a conic or
one projected coordinate list. The genuine flat ring
and its prime reduced exceptional pullbacks remain
essential at higher-multiplicity plinth points.
The simultaneous-zero fiber, residual global quadratic
recognition, moving frames and universal-frame reduction
remain unresolved. No novelty or unrestricted solution
follows from these conditional exclusions.

## Sources

[^1]: Shulim Kaliman and Nikolai Saveliev, [*C+-actions on contractible threefolds*](https://www.math.miami.edu/~kaliman/library/KaSa.michigan.2004.quotient.pdf), Lemma 2.1, Theorem 2.7 and Corollary 2.8; [Stacks Project 00R4](https://stacks.math.columbia.edu/tag/00R4), miracle flatness. The exact cylinder-to-domination and flatness arguments are in the [intrinsic quotient note](research/intrinsic-quotient-surface-pass.md). The target ring is not assumed polynomial.
[^2]: The Stacks Project, [Section 59.26, especially Definition 59.26.3 and its following proof](https://stacks.math.columbia.edu/tag/03PA), the monic-polynomial/invertible-derivative criterion for a standard étale algebra. The specific slice formulas and derivative obstruction above are separate calculations.
[^3]: Shulim Kaliman, [*Free C+-actions on C3 are translations*](https://www.math.miami.edu/~kaliman/library/Ka.invent.2004.c%2B.pdf), *Inventiones Mathematicae* 156 (2004), 163–173, exceptional factorization and Proposition 3.2 homology diagram. The [pass49 normalized-cover note](research/normalized-cover-surjectivity-pass49.md) and its re-audit give the additional deduction under the actual hypotheses; it is not attributed verbatim to the published paper.
