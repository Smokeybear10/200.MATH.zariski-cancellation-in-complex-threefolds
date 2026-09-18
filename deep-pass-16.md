# Invariant slices, triangular derivations, and the remaining cancellation gap

## Result and scope

For every triangular derivation
\[
D=p(x)\partial_y+P(x,y)\partial_z,
\qquad 0\ne p\in\mathbb C[x],\quad P\in\mathbb C[x,y],
\]
on \(R=\mathbb C[x,y,z]\), let \(C=\ker D\), and take any
\(A,B\in C\). The extension \(E=AD+B\partial_t\) satisfies
\[
\boxed{
 E\text{ has a polynomial slice}
 \iff E\text{ has a slice affine in }t
 \iff AP_D+BC=C,\qquad P_D=D(R)\cap C.
}
\tag{1}
\]
The proof below covers arbitrary degrees, repeated roots, singular
coefficient curves, and zero-coefficient boundary cases. It is a complete
working proof of this restricted assertion, not a solution of the
complex threefold cancellation conjecture.

The precise plinth formula used below is already in Dasgupta and Lahiri's
July 2026 manuscript. It is reconstructed here and attributed to that
source.[^1] No novelty claim is made for (1). Recognizing the polynomial
kernel in this invariant-coordinate setting is also covered by prior
results, as explained in the
[coordinate-partial audit](research/commuting-coordinate-partial-pass.md).
The issue addressed by (1) is the existence of an affine replacement in
the specified original variable, not merely recognition of the kernel.

Section 9 extends affine replacement to all base derivations whose
higher image ideals are principal. With the published rank-at-most-two
freeness result as an external input, this includes nontriangular bases
fixing an ambient coordinate. The original source proof for that input
is not reconstructed here; the access and attribution boundary is explicit.

Two further conclusions delimit a possible extension of (1). A minimal
nonlinear slice on a polynomial threefold base would force a nonprincipal
higher image ideal. A concrete
localized example has a cubic slice but no affine replacement, so the
global polynomial-base hypothesis cannot simply be discarded.

The unrestricted target remains
\[
X\times_{\mathbb C}\mathbb A^1\simeq\mathbb A^4
\quad\Longrightarrow\quad X\simeq\mathbb A^3.
\tag{2}
\]
The interpretation of Luo's dimensional typo has not been confirmed by
him. Nothing here establishes that every case of (2) admits the displayed
triangular presentation, or even an arbitrary invariant-coefficient
extension presentation. Human expert review and proof-assistant
verification have not occurred.

## 1. Definitions and the elementary affine criterion

A locally nilpotent derivation is a derivation for which every polynomial
is killed by some iterate. A slice is a polynomial \(s\) satisfying
\(E(s)=1\). In characteristic zero the slice theorem gives
\(R[t]=(\ker E)[s]\). This follows by induction on derivation degree,
subtracting the appropriate invariant multiple of the highest power of
\(s\). A slice is a translation parameter over its kernel; the slice
theorem alone does not identify that kernel as a polynomial ring.

The plinth ideal consists of the invariant values of \(D\). It measures
where a local slice can be divided by its derivative to give an actual
slice. If \(A\ne0\), an affine candidate \(r+ht\) satisfies
\[
E(r+ht)=ADr+Bh+(ADh)t.
\]
It is a slice precisely when \(Dh=0\) and \(ADr+Bh=1\).
Applying \(D\) to the latter equality gives \(D^2r=0\), since the
ring is a domain and \(A\ne0\). Thus affine slices are equivalent to
\(AP_D+BC=C\). This coefficient argument works for arbitrary base
LNDs. The substantive direction of (1) replaces a potentially nonlinear
slice by an affine one.

## 2. Primitive normalization and the invariant ring

Let \(h\) be the monic gcd of \(p\) and all coefficients of \(P\)
as a polynomial in \(y\). When \(P=0\), use the monic associate of
\(p\). Write
\[
p=ha,\qquad P=hP_1,\qquad D=h\delta,
\qquad \delta=a(x)\partial_y+P_1(x,y)\partial_z.
\tag{3}
\]
Choose \(Q_y=P_1\) with \(Q(x,0)=0\), and put
\[
F=a(x)z-Q(x,y),\qquad C=\mathbb C[x,F].
\tag{4}
\]
Here is a direct verification of the kernel equality in (4). After
inverting \(a\), the coordinates are \(x,F,y\), and the derivation
is \(a\partial_y\). Its kernel is \(\mathbb C[x,1/a,F]\).
At every root \(\alpha\) of \(a\), the gcd choice ensures that
\(P_1(\alpha,y)\ne0\), hence \(Q(\alpha,y)\) is nonconstant.
Consequently substitution \(F\mapsto-Q(\alpha,y)\) is injective on
\(\mathbb C[F]\). Any minimal denominator involving \(x-\alpha\)
would therefore force its numerator to be divisible by the same factor
already in \(\mathbb C[x,F]\). Removing these factors proves (4).

The quotient map is surjective on complex points. If \(a(\alpha)\ne0\),
solve for \(z\). Otherwise solve the nonconstant polynomial equation
\(Q(\alpha,y)+\nu=0\), with \(z\) arbitrary. In particular, a
common zero of \(A\) and \(B\) lifts to a fixed point of \(E\).
Therefore every slice forces
\[
(A,B)C=C.
\tag{5}
\]

## 3. Exact plinth formula and its reconstruction

Partition the roots of \(a\) into good roots, where
\(P_1(\alpha,y)\) is a nonzero constant, and bad roots, where it
is nonconstant. Define
\[
g_{\rm bad}=
\prod_{\alpha\ {m bad}}(x-\alpha)^{\operatorname{ord}_\alpha a}.
\]
The empty product is one. Then
\[
\boxed{P_\delta=g_{\rm bad}C,\qquad P_D=h g_{\rm bad}C.}
\tag{6}
\]
For the primitive derivation, this is the specialization of
Dasgupta and Lahiri, Proposition 5.6(i), Lemma 5.8, and Theorem 5.9(I),
to the PID \(\mathbb C[x]\). Their additional higher-image formulas
have extra hypotheses and are not assumed here.[^1]

At a good root, set \(q=x-\alpha\), \(a=q^nu\), and
\(Q=cy+qH\), where \(c\ne0\) and \(u(\alpha)\ne0\).
Starting with \(I_0=-F/c\), iterate
\[
I_{j+1}=-F/c-(q/c)H(x,I_j),\qquad I=I_{n-1}.
\]
Each update improves \(I_j-y\) by one power of \(q\), up to the
error \(q^nuz/c\). Thus
\[
r_\alpha=\frac{y-I(x,F)}{q^n}\in R,
\qquad \delta r_\alpha=u=a/q^n.
\tag{7}
\]
This is a polynomial in the original ring. In particular it introduces
no inverse of another root factor. The gcd in \(\mathbb C[x]\) of
\(a\) and all the witnesses \(a/q^n\) from good roots is a
nonzero constant multiple of \(g_{\rm bad}\). Bezout combinations
therefore give \(g_{\rm bad}\in P_\delta\).

For the reverse inclusion, let \(\delta r=g\in C\). The generic
presentation gives
\[
r=(g/a)y+H_0(x,F),\qquad H_0\in C[1/a].
\tag{8}
\]
Fix a bad root \(\alpha\) of multiplicity \(n\). Suppose that
\(g\) is not divisible by \(q^n\) in \(C\). Clear the largest
\(q\)-pole in the two summands of (8), and reduce at \(q=0\).
An unmatched pole cannot vanish because substitution by
\(-Q(\alpha,y)\) is injective. Equal poles would require
\[
yG(-Q(\alpha,y))+H_1(-Q(\alpha,y))=0,
\qquad G\ne0.
\]
If \(d=\deg_yQ(\alpha,y)\ge2\), the first nonzero term has
degree congruent to one modulo \(d\), while the second has degree
congruent to zero. They cannot cancel. Hence \(q^n\mid g\) for
every bad root, proving the first equality in (6). Finally
\(D=h\delta\) and invariance of \(h\) give \(P_D=hP_\delta\),
which proves the second equality. This reconstruction does not assert
originality for the formula.

## 4. Why a slice cannot meet a bad quotient line

Let
\[
\Sigma=\{\alpha:h(\alpha)=0\}\cup\{\alpha:\alpha\text{ is bad}\}.
\]
The exact slice criterion can now be written without an unknown ideal:
\[
\boxed{
E\text{ has a slice}
\iff (A,B)C=C\ \text{and}\
B(\alpha,F)\in\mathbb C^*\quad\text{for every }\alpha\in\Sigma.
}
\tag{9}
\]
We prove necessity before constructing the affine slice.

At a root of \(h\), \(D\) vanishes on the whole plane
\(x=\alpha\). Surjectivity of the quotient means a zero of
\(B(\alpha,F)\) gives an \(E\)-fixed point, contradicting a
slice. At a bad root, if \(B(\alpha,F)\) vanishes identically,
choose a root of \(P_1(\alpha,y)\) to obtain the same contradiction.

It remains to exclude a nonzero, nonconstant \(B(\alpha,F)\).
Choose one of its roots \(\nu\), and an irreducible component
\(b=0\) of \(B=0\) through \((\alpha,\nu)\). This component
is not the line \(x=\alpha\). Normalize the curve and choose a
point above \((\alpha,\nu)\). Its local ring \(V\) is a DVR
with residue field \(\mathbb C\). These normalization properties
hold for affine integral curves, including singular ones.[^2][^3]

In \(V\), the element \(q=x-\alpha\) is nonzero and nonunit;
the other root factors of \(a\) are units. If \(L\) is the
fraction field and \(\pi\) a uniformizer, the base-change ring is
\[
T=V[y,z]/(a(x)z-Q(x,y)-F),
\quad T_L=L[y],
\quad T/\pi T=\mathbb C[y,z]/(Q(\alpha,y)+\nu).
\tag{10}
\]
The relation defining \(T\) is primitive and linear in \(z\)
over the UFD \(V[y]\). Its coefficients are coprime because
\(Q(\alpha,y)+\nu\) is nonconstant. Gauss's lemma therefore
makes \(T\) a domain.

The generic derivation has kernel \(L\). An element of
\(T\cap L\) with negative valuation would make \(\pi\)
invertible in \(T\), contradicting the nonzero special fiber.
Thus \(\ker\delta_V=V\). This explicitly proves the needed
kernel equality; it does not assume invariants commute with arbitrary
base change.

A \(\delta_V\)-slice would give \(T=V[s]\). The special fiber
would then be \(\mathbb C[s]\). But the polynomial in (10) has
degree at least two. With multiple distinct roots its quotient has
nontrivial idempotents; with one distinct root it has a nonzero
nilpotent. Both contradict a polynomial-line fiber.

Finally, an \(E\)-slice survives base change. Since \(B=0\)
in \(V\), evaluate its constant \(t\)-coefficient to get
\(\overline A\,\overline h\,\delta_V(S_0)=1\). Multiplication
by the invariant \(\overline A\,\overline h\) gives a
\(\delta_V\)-slice, a contradiction. This treats tangencies,
singularities and repeated factors of \(B\) without further assumptions.

## 5. Constructing the affine slice and handling boundaries

Condition (9), formula (6), and Nullstellensatz give
\((A,B)C=C\) and \((P_D,B)C=C\). Choose
\[
AU+BV=1,\qquad p_0+BW=1,\qquad p_0\in P_D.
\]
Multiplication yields
\[
1=AUp_0+B(AUW+Vp_0+BVW).
\tag{11}
\]
Choose \(r\in R\) with \(Dr=Up_0\). Then
\[
s=r+(AUW+Vp_0+BVW)t
\]
is the required affine slice. Conversely, any such slice satisfies
the elementary ideal condition in Section 1. This proves (1) and (9).

If \(A=0\), a slice exists exactly when \(B\) is a nonzero
constant, and \(t/B\) is one. If \(B=0\), existence forces
\(A\) to be a unit and \(D\) to have a slice, by taking the
constant \(t\)-coefficient. Both zero gives no slice. Constant
nonzero \(p\) and \(P=0\) are already included in (3)-(11).

For an explicit mixed-root example, let
\[
a=x^2(x-1)^3,\quad h=x+1,\quad
D=ha\partial_y+h(1+xy)\partial_z,
\quad F=az-y-xy^2/2.
\]
The root zero is good; the root one is bad; minus one is a replica
zero. Put
\[
r=(y+F+xF^2/2)/x^2,\qquad
g=(x+1)(x-1)^3,\qquad V=(g+1)/x.
\]
Both displayed quotients are polynomials, \(Dr=g\), and
\((D+x\partial_t)(-r+Vt)=1\). The coefficient \(B=x\) takes
different nonzero values on the two excluded lines. A single scalar
congruence modulo their product is not being assumed.

## 6. Higher-image torsion for arbitrary base derivations

Now let \(D\ne0\) be any LND on \(\mathbb C^{[3]}\), put
\(C=\ker D\), and take nonzero invariant \(A,B\). Set
\(\delta=AD\) and \(I_n=\delta^n(R)\cap C\). These are
the same image ideals obtained by applying \(\delta^n\) to
\(\ker\delta^{n+1}\). Suppose a slice of minimal degree in
\(t\) has degree \(n\ge2\), with leading coefficient \(c\).
The coefficient recurrence gives
\[
c\in C,\qquad \delta^n s_0=(-1)^n n!B^n c.
\tag{12}
\]
Thus \(B^n c\in I_n\). If \(c=\delta^n u\), then
\[
J_u=\sum_{j=0}^n\frac{(-1)^j}{j!}B^{n-j}t^j\delta^j u
\tag{13}
\]
is a polynomial invariant of \(E\), with leading coefficient
\((-1)^n c/n!\). Subtracting \((-1)^n n!J_u\) from the
slice lowers its degree, contrary to minimality. Therefore
\[
\boxed{c\notin I_n,\qquad B^n c\in I_n.}
\tag{14}
\]
If \((I_j:B)=I_j\) for every \(j\ge2\), nonlinear minimum
degree is impossible. A given degree-\(N\) slice only requires this
saturation for \(2\le j\le N\). The finite sum (13) is verified
by termwise cancellation; no variable-time exponential is presumed to
be an automorphism.

The faithful flatness of the complex three-space quotient implies
\((A,B)C=C\) for a slice extension, as also shown in the
[quotient-slice analysis](research/quotient-slice-boundary-pass15.md).
Writing \(J_n=D^n(R)\cap C\), we have \(I_n=A^nJ_n\).
Equation (12) and comaximality force \(c=A^nc_0\); (14) becomes
\(c_0\notin J_n\), \(B^nc_0\in J_n\).

Moreover \(\sqrt{J_n}=\sqrt{P_D}\): one inclusion follows from
\(J_n\subseteq P_D\); for the other use
\(D^n(r^n)=n!(Dr)^n\) whenever \(Dr\in P_D\).
If \(J_n\) is principal and \(B\) shares no irreducible factor
with the plinth generator, it is automatically \(B\)-saturated
in the UFD \(C\). Hence a minimal nonlinear slice with that
coprimality would force a nonprincipal higher image ideal. Principality
of every such ideal is the Freeness Conjecture recalled by Dasgupta and
Lahiri, not a theorem available for arbitrary LNDs.[^1]

Freudenburg's Proposition 7.1 already uses precisely a higher-image
saturation hypothesis to describe invariant extensions. It does not
establish the hypothesis in general.[^4] The elementary deduction
(12)-(14) is useful for locating the obstruction, not a claim that
the older hypothesis can be removed.

## 7. A genuine localized failure of affine replacement

Let \(v=x^2z-y^2\) and
\[
R'=\mathbb C[x,y,z,v^{-1}],\qquad
D=x^2\partial_y+2y\partial_z,\qquad E=D+x\partial_t.
\]
Then
\[
s=\frac{-yz+3xzt-3yt^2+xt^3}{2v}
\quad\text{satisfies}\quad E(s)=1.
\tag{15}
\]
For a short derivation, set \(\rho=y-xt\), \(Z=z-t^2\), and
\(w=xZ-2\rho t\). Directly \(E\rho=Ew=Ev=0\),
\(EZ=2\rho\), and \(v=xw-\rho^2\). Thus
\(s=(wt-\rho Z/2)/v\) gives (15).

Formula (6) gives \(P_D=(x^2)\) before localization. Invariant
localization preserves this ideal, and \((x^2,x)\) remains proper
in \(\mathbb C[x,v,v^{-1}]\). The elementary affine criterion
therefore rules out every affine-in-\(t\) slice on \(R'[t]\).
This is an actual nonlinear-slice example, not just torsion in an ideal.
It is not a counterexample on \(\mathbb C^{[3]}\), because the
denominator \(v\) is essential. It also gives no cancellation
counterexample.

## 8. The general geometric route and a failed shortcut

For arbitrary \(D\), suppose a component of \(B=0\) is not
contained in the plinth support. Normalize it and take a DVR \(V\)
over an intersection point with that support. Faithful flatness of
the polynomial-threefold quotient gives a faithfully flat domain
\(T=R\otimes_CV\), with generic fiber a polynomial line.
The no-pole argument again proves \(\ker D_V=V\). A slice
extension would therefore imply \(T=V[s]\), and in particular
a reduced affine-line special fiber with a nonzero translation action.

The missing implication is that such a single fiber must lie outside
the plinth support. Masuda's principal-plinth theorem describes general
fibers along a plinth component, not every special point.[^5] The more
recent faithfully flat quotient result identifies the **closure** of
the bad-fiber set with plinth support for an irreducible derivation.
It does not replace that closure by pointwise equality.[^6]

Finiteness of an intermediate map does not by itself repair the gap.
Consider
\[
Y=\operatorname{Spec}\mathbb C[t,(t+1)^{-1},y],\qquad u=t^2,
\]
factored through
\[
Z=\operatorname{Spec}\mathbb C[u,w]/(w^2-u(u-1)^2),
\quad \kappa(t,y)=(t^2,t(t^2-1)),\quad\theta(u,w)=u.
\tag{16}
\]
The map \(\theta\) is finite of degree two. The map \(\kappa\)
is surjective with reduced affine-line fibers. Nevertheless the generic
fiber over \(u\) has two affine lines, while the fiber over \(u=1\)
has only the retained line \(t=1\), and is smooth there. The other
normalization branch \(t=-1\) has been removed. The singular node
of \(Z\) allows these facts to coexist.

This rejects an abstract finite-factorization inference. The map
\(Y\to\mathbb A^1_u\) is not its additive-action invariant
quotient, and this is not the specific proper compactification
factorization in Kaliman's proof. Those distinctions are necessary.
The detailed [source audit](research/invariant-slice-literature-pass16.md)
also explains the whole-exceptional-component fixed-point deduction
from Kaliman's local branch argument.[^7] Section 9 completes the
support identification needed to use that deduction for arbitrary
base derivations. It still does not establish a pointwise fiber criterion.

## 9. Whole-component exclusion and the rank-two corollary

Let \(D\ne0\) now be arbitrary on \(\mathbb C^{[3]}\), and let
\(p_D\) generate its plinth ideal. Then
\[
\boxed{AD+B\partial_t\text{ has a slice}
\quad\Longrightarrow\quad\gcd_C(B,p_D)=1.}
\tag{17}
\]
This excludes a shared curve component. It is weaker than
\((B,p_D)C=C\): two coprime plane polynomials can still have
isolated common zeros.

Here is the source-dependent proof. Kaliman's retained exceptional
curve \(\Gamma\) has a product quotient off the curve. Its actual
finite factorization has generic degree greater than one on every
retained component, and the local ramification/transversal argument
forces a fixed point above each component.[^7] The
[whole-component reconstruction](research/whole-plinth-component-pass16.md)
details why this uses local freeness at a chosen point, not an assumed
globally free action or arbitrary normalization ramification.

Suppose first that \(D\) is primitive. Write \(\Gamma=V(f)\).
The product gives \(R_f=C_f[u]\) and \(D=a\partial_u\) for
\(a\in C_f\). If \(a\) had a nonunit prime factor \(q\),
that factor would divide every original coefficient of \(D\) in
\(R_f\). Factorial closure of \(C\) in \(R\), together with
the UFD property and \(q\nmid f\), descends this divisibility to
\(R\), contrary to primitivity. Hence \(a\) is a unit. Clearing
the denominator of the local slice \(u/a\) gives \(f^N\in P_D\)
for some \(N\), and therefore \(V(P_D)\subseteq\Gamma\).

Conversely, the generic multiple-line fibers on every component of
\(\Gamma\) preclude any plinth value nonzero generically there.
Thus \(V(P_D)=\Gamma\). If \(B\) shared a component with this
support, its fixed point supplied above would also be a zero of
\(AD+B\partial_t\), contradicting a slice. This proves (17)
for primitive \(D\).

For a replica \(D=hD_0\), primitive normalization has
\(h\in\ker D_0=C\) and \(P_D=hP_{D_0}\). The primitive
argument applies to the extension \((Ah)D_0+B\partial_t\).
A common factor of \(B\) and \(h\) is also impossible: above
its zero curve the original derivation and \(B\) both vanish,
and quotient surjectivity supplies an actual fixed point. This proves
(17) in full generality.

Combining (17) with (14) gives the conditional theorem
\[
\boxed{
\bigl[D^j(R)\cap C\text{ is principal for every }j\ge2\bigr]
\ \Longrightarrow\
\bigl[E\text{ has a slice}\iff AP_D+BC=C\bigr].
}
\tag{18}
\]
Indeed a generator of each higher image ideal has exactly the plinth
generator's irreducible factors, by radical equality. Equation (17)
makes each ideal \(B\)-saturated. The minimal-degree torsion
obstruction then rules out a nonlinear minimum. The resulting affine
slice gives the unit-ideal condition. No pointwise geometric bridge is
needed for this conditional conclusion.

Ben Khaddah, El Kahoui and Ouali's published result establishes the
freeness property for rank-at-most-two LNDs in characteristic zero.[^8]
Its adapted kernel basis gives principal higher image ideals: if
\(\deg_D e_i=i\), then \(\ker D^{j+1}\) is spanned over
\(C\) by \(e_0,\ldots,e_j\), and the image ideal is
\((D^j e_j)C\). Therefore (18) applies to every such base derivation,
not just triangular ones. This is a corollary using a published input,
not a new proof of that input or a new polynomial-kernel recognition
theorem. The [source-boundary note](research/rank-two-image-ideals-pass16.md)
distinguishes the verified publisher statement from the original full
proof, which is not reproduced.

In particular, any genuine failure of affine replacement for an
invariant extension on \(\mathbb C^{[3]}\) would have a rank-three
base and a nonprincipal higher image ideal. The general Freeness
Conjecture would rule out that failure. This is not a proof of either
conjecture. The May 2026 factorial-domain classification also explicitly
assumes the freeness property; it does not supply it for every base.[^9]

## 10. Verification and unresolved work

The independent symbolic controls are in
[invariant_slice_checks.py](research/invariant_slice_checks.py). They
check displayed slices, finite inverses, mixed and nonmonic repeated
roots, degree-obstruction examples, the localized cubic identity, and
the nodal countercontrol. The all-degree and geometric conclusions
depend on the written proofs above, not on counting these tests.

Reproduce the new suite with:

```sh
/opt/anaconda3/bin/python research/invariant_slice_checks.py
```

All 352 test methods in 24 suites passed. The complete regression
results and commands are recorded in
[verification-pass-16.json](verification-pass-16.json). Separate proof
reconstructions are available in the
[triangular note](research/invariant-affine-controls-pass16.md) and
[higher-image note](research/invariant-affine-slice-pass16.md).
The code does not import a research solver. Passing symbolic identities
does not constitute Lean verification, a peer-reviewed theorem, or
proof of (2).

The remaining affine-replacement issue is now confined to rank-three
bases with a possible failure of higher-image principality. A direct
alternative is the pointwise reduced-fiber implication for actual
polynomial-threefold quotients; the whole-component result does not
settle isolated intersections. The published rank-two result removes
the need to search further for a counterexample in that class.
Even resolving affine replacement for arbitrary invariant extensions
would leave both the affine-slice coordinate-lifting problem and the
global reduction of arbitrary slice derivations to that frame.
The current evidence does not justify saying that only a routine final
step remains.

## Sources

[^1]: Nikhilesh Dasgupta and Animesh Lahiri, [*On image ideals of nice and quasi-nice derivations on R[X1,X2]*](https://arxiv.org/html/2302.13787v6), arXiv:2302.13787v6, July 24, 2026. Proposition 5.6(i), Lemma 5.8, Theorem 5.9(I), and the introductory formulation of the Freeness Conjecture. The theorem's higher-image part is not used without its additional hypotheses.

[^2]: The Stacks Project, [Lemma 33.41.2, Tag 0C1R](https://stacks.math.columbia.edu/tag/0C1R), normalization of reduced Nagata curves. Finite, surjective normalization is the fact used here.

[^3]: The Stacks Project, [Lemma 33.27.6, Tag 0C3P](https://stacks.math.columbia.edu/tag/0C3P), including the proof identifying one-dimensional normal local rings as DVRs in this setting.

[^4]: Gene Freudenburg, [*Actions of SL2(k) on Affine k-Domains and Fundamental Pairs*](https://arxiv.org/pdf/2108.12021), arXiv:2108.12021v2, June 2022. Section 7.1, Proposition 7.1. Used for comparison of the explicit saturation hypothesis, not as a general slice-replacement theorem.

[^5]: Kayo Masuda, [*Factorial affine Ga-varieties with principal plinth ideals*](https://arxiv.org/html/2312.05455v1), arXiv:2312.05455v1, December 2023. Theorem 3.9, with its irreducibility and generic-fiber qualifications.

[^6]: Kayo Masuda, [*Faithfully flat quotient morphisms by Ga-actions on factorial affine varieties*](https://arxiv.org/html/2512.06687v1), arXiv:2512.06687v1, December 7, 2025. Proposition 2.5(3) and the following remark, used with an irreducible derivation. The relevant statement takes closure of the bad-fiber locus.

[^7]: Shulim Kaliman, [*Free C+-actions on C3 are translations*](https://www.math.miami.edu/~kaliman/library/Ka.invent.2004.c%2B.pdf), Inventiones Mathematicae 156 (2004), 163-173, final author manuscript. Lemma 2.2, Proposition 3.2, and the proof of Proposition 4.2; numbering differs from the older arXiv version.

[^8]: A. Ben Khaddah, M. El Kahoui and M. Ouali, [*The Freeness Property for Locally Nilpotent Derivations of R[2]*](https://link.springer.com/article/10.1007/s00031-022-09705-z), Transformation Groups 28 (2023), 35-60; published online March 5, 2022. The publisher abstract states the PID and rank-at-most-two results. The explicit image-ideal formulation and attribution to Theorem 4.1 are corroborated in Dasgupta-Lahiri's introduction; the original full proof remains an external input.

[^9]: M'hammed El Kahoui, Hatim Labtaini and Mustapha Ouali, [*The Freeness Property for Locally Nilpotent Derivations of Factorial Domains*](https://link.springer.com/article/10.1007/s00031-026-09969-9), Transformation Groups, published May 15, 2026. The publisher abstract's freeness assumption is the limited fact used here.
