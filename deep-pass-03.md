# Slice classification for extensions of a rank-three derivation

A complete working proof is given below for a specified family of locally
nilpotent derivations on four-dimensional affine space. The coefficient family
is the full polynomial algebra `k[x,f,g]`, with `f,g` defined below. The criterion
is finite and constructive: it decides whether a polynomial slice exists and
produces a coordinate slice in every positive case.

This is a family-specific result. It does not prove or disprove
`X × A¹ ≅ A⁴ ⇒ X ≅ A³` over the complex numbers. Originality is unestablished;
the result is not presented as a new published theorem. The explicit
rank-three derivation is due to Freudenburg, not introduced here.[^1]

## 1. Statement and scope

Let `k` be any field of characteristic zero, and put

\[
R=k[x,y,z],\quad f=xz-y^2,\quad
g=zf^2+2x^2yf+x^5,\quad r=-x^3-fy,
\]

\[
\Delta=\operatorname{Jac}(f,g,\cdot),\qquad
A=k[f,g],\qquad C=k[x,f,g].
\]

For `P∈C`, differentiate with respect to `x` while holding `f,g` fixed and define

\[
L(P)=gP+2(xg-f^3)P_x,\qquad
M=(f,g-x^5)C+x^2A.
\tag{1}
\]

The sum defining `M` is a sum of `A`-submodules, not an assertion that `x²A`
is an ideal of `C`.

**Family theorem.** For every `a∈C`, the following are equivalent:

1. `D_a=Δ+a∂w` on `R[w]` has a polynomial slice, meaning `D_a(s)=1`.
2. There exist `c∈k×` and `H∈R` such that `a=c+ΔH`.
3. There exist `c∈k×` and `P∈M` such that `a=c+L(P)`.

Every positive case has the coordinate slice `(w-H)/c` and kernel isomorphic
to `k` in three polynomial variables. Furthermore, the action is free exactly
when `a(0,0,0)≠0`, where the three arguments here are the formal variables
`x,f,g`. Thus freeness alone is insufficient, even inside this restricted family.

There is also an exact primitive formula:

\[
\Delta(R)\cap C=L(M).
\tag{2}
\]

The family theorem classifies arbitrary slice degrees. It does not follow merely
from failing to find a primitive or a slice in a finite search. Its negative
direction uses the orbit and special-fiber arguments below.

## 2. Identities and the cancellation connection

Direct differentiation gives

\[
\begin{aligned}
\Delta x&=2fr,&\Delta y&=-g-6x^2r,&
\Delta z&=2xf^2-10xyr,\\
\Delta f&=0,&\Delta g&=0,&\Delta r&=fg,\\
r^2+f^3&=xg.
\end{aligned}
\tag{3}
\]

The nonzero Jacobian `Jac(x,f,g)=2fr` shows that `x,f,g` are algebraically
independent, so `C` really is a polynomial algebra. After inverting `fg`,

\[
x=\frac{r^2+f^3}{g},\qquad
y=-\frac{r+x^3}{f},\qquad
z=\frac{g+2rx^2+x^5}{f^2}.
\tag{4}
\]

Consequently `R[1/(fg)]=k[f±¹,g±¹,r]`, with derivation `fg∂r`. This proves
local nilpotence on `R`; the extension `D_a` is locally nilpotent as well,
since its successive derivatives of `w` are successive `Δ`-derivatives of `a`.

The fixed locus of `Δ` is precisely `x=y=0`. Indeed, a common zero of its
coordinate images also has `Δr=fg=0`. If `f≠0`, then `g=r=0`, contradicting
`r²+f³=xg`. If `f=0`, then `r=-x³`, `g=x⁵`, and `Δy=5x⁵`, forcing `x=y=0`.
The converse follows from the displayed images. Every coefficient in `C`
restricts to its constant value at `x=f=g=0` on this line. In characteristic
zero a nonzero additive-group vector field has no nontrivial finite stabilizer,
which gives the asserted freeness criterion.

The standard slice theorem says `R[w]=(ker D_a)[s]` when `D_a(s)=1`.[^1]
For the general cancellation problem, a slice with a nonpolynomial kernel on
affine four-space would be a counterexample. The family theorem shows that no
such example occurs here. It does not establish that every derivation relevant
to cancellation belongs to this family.

If `a=c+ΔH`, set `s=(w-H)/c`. In coordinates `(x,y,z,s)`, the derivation is
`Δ+∂s`. Let `Φ_t` be the finite polynomial flow of `Δ`. Then

\[
(u_1,u_2,u_3)=\Phi_{-s}(x,y,z)
\]

together with `s` form polynomial coordinates. The inverse is
`(x,y,z)=Φ_s(u₁,u₂,u₃)` and `w=cs+H(Φ_s(u₁,u₂,u₃))`. Hence the kernel is
exactly `k[u₁,u₂,u₃]`. This verifies the constructive positive direction.

## 3. Exact polynomial primitives

Equation (3) implies

\[
\Delta(rP)=fL(P).
\tag{5}
\]

Two useful fractions are actual polynomials:

\[
\tau=\frac{g-x^5}{f}=2x^2y+fz,
\qquad S=\frac{rx^2+g}{f}=x^2y+fz.
\tag{6}
\]

If `P=fP₁+(g-x⁵)P₂+x²Q`, with `P₁,P₂∈C` and `Q∈A`, then

\[
H=rP_1+r\tau P_2+QS=\frac{rP+gQ}{f}\in R
\tag{7}
\]

satisfies `ΔH=L(P)`. This proves one inclusion in (2).

For the converse, suppose `ΔH=a∈C` with `H∈R`. The localization `R_f` is a
free `C_f`-module with basis `1,r`, subject to `r²=xg-f³`. The quadratic is
irreducible over `k(x,f,g)`, because `xg-f³`, viewed as a rational function
of `x` over `k(f,g)`, has a simple zero and cannot be a square. Retaining `x`,
the formulas for `y,z` in (4) supply the inverse presentation after inverting
`f` only; the displayed formula dividing by `g` is not needed here.

Write `H=U+rV` with `U,V∈C_f`. Odd and even powers of `r` in its derivative
give `U_x=0` and `L(fV)=a`. Thus `U∈A_f`. The operator `L` is invertible on
`k(f,g)[x]`: for `a=Σa_jx^j` its unique inverse `P=Σp_jx^j` satisfies

\[
p_d=\frac{a_d}{(2d+1)g},\qquad
p_j=\frac{a_j+2(j+1)f^3p_{j+1}}{(2j+1)g}.
\tag{8}
\]

This recursion puts `P` in `C_g`, while `P=fV` belongs to `C_f`. Since `C`
is a polynomial ring in the independent variables `x,f,g`, their intersection
is `C`. Therefore `P∈C` and `H=rP/f+U`.

The invariant term `U` has at most a simple pole in `f`. A minimal denominator
`f^m` with `m>1`, after multiplying the last identity by `f^m` and reducing
modulo `f`, would make a nonzero polynomial in `g` vanish. This is impossible
because `g≡x⁵ mod f`. Consequently `U=Q₀/f` with `Q₀∈A`.

Polynomiality of `H` now implies

\[
x^3P(x,0,x^5)=Q_0(0,x^5)\in k[x^5].
\tag{9}
\]

This is equivalent to `P(x,0,x⁵)∈x²k[x⁵]`. The kernel of the evaluation
`C→k[x]`, `f↦0,g↦x⁵`, is `(f,g-x⁵)C`; hence (9) is exactly `P∈M`.
This proves (2).

The finite primitive test is therefore: compute (8), reject genuine
`g`-denominators, and otherwise check that every nonzero monomial of
`P(x,0,x⁵)` has exponent congruent to two modulo five. Accepted inputs have
the polynomial primitive (7).

## 4. The first-pole obstruction

The following stronger lemma handles coefficients outside `C` as well.

**First-pole lemma.** Suppose `H∈R`, `f` divides `ΔH`, and `c∈k×`. The
residue of `H` modulo `f` is a unique polynomial `h(x)`. Then

\[
\Delta+\left(c+\frac{\Delta H}{f}\right)\partial_w
\text{ has a polynomial slice}
\quad\Longleftrightarrow\quad h\in k[x^5].
\tag{10}
\]

To see the residue assertion, reduce `Δ` on the domain
`R/(f)=k[x,y,z]/(xz-y²)`. Localizing at `x` gives `k[x±¹,y]` with derivation
`5x⁵∂y`, whose kernel is `k[x±¹]`. A Laurent polynomial with a genuine pole
in `x` cannot belong to the unlocalized cone ring: clear its smallest
denominator and reduce modulo `x` to obtain an impossible nonzero scalar.
Thus the kernel before localization is `k[x]`, and `H=h(x)+fK` for some `K∈R`.

If `h=P(x⁵)`, the polynomial `H-P(g)` is divisible by `f`. Its quotient `K'`
has `ΔK'=ΔH/f`, so `(w-K')/c` is a coordinate slice.

For necessity extend scalars to an algebraic closure and assume `h∉k[x⁵]`.
Choose a primitive fifth root of unity `ζ`. The polynomial

\[
F(B)=c(1-\zeta^3)+B^2\bigl(h(\zeta B)-h(B)\bigr)
\tag{11}
\]

has positive degree and nonzero constant term. It therefore has a nonzero
root `b`. Set `d=b⁵`. The equation

\[
X^6-dX+\epsilon^3=0
\tag{12}
\]

has formal power-series solutions `x₁(ε),x₂(ε)` with constants `b,ζb`.
At both constants its derivative is `5d≠0`. Recursive coefficient comparison
therefore determines each successive coefficient uniquely; this is the simple
root form of Hensel lifting.[^2] Both solutions are units of `k̄[[ε]]`.

Let `p_i=(x_i,0,ε/x_i)`. Equation (12) gives `f(p_i)=ε`, `g(p_i)=d`, and
`r_i=-x_i³`. The time

\[
T=\frac{r_2-r_1}{\epsilon d}
\tag{13}
\]

has a pole of order one, since its numerator has constant
`b³(1-ζ³)≠0`. It takes the `Δ`-orbit from `p₁` to `p₂`: `r` changes by
`fgT`, and equations (4) then identify every endpoint coordinate.

For the extended derivation the fourth-coordinate displacement is

\[
W=cT+\frac{H(p_2)-H(p_1)}\epsilon
=\frac{c(r_2-r_1)/d+H(p_2)-H(p_1)}\epsilon.
\tag{14}
\]

The numerator has zero constant term by (11), so `W∈k̄[[ε]]`. Thus both
`(p₁,0)` and `(p₂,W)` have integral coordinates, although their translation
time does not. A polynomial slice would satisfy

\[
s(p_2,W)-s(p_1,0)=T.
\tag{15}
\]

The left side is a power series without a pole, a contradiction. A slice over
the original field would remain one after scalar extension. This proves (10)
in every degree.

In the form `H=h(x)+fK`, a polynomial shear reduces the coefficient to
`c+2r h'(x)`. Hence this normalized extension has a slice exactly when
`h∈k[x⁵]`. Each such action is free, because its coefficient equals `c`
on the fixed line of `Δ`.

Applying the lemma to `H=rP` gives the complete classification in the
subfamily `a=c+L(P)`: its residue is `h(x)=-x³P(x,0,x⁵)`, so (10) is exactly
the condition `P∈M`.

## 5. Excluding every complementary coefficient in C

It remains to show that a slice forces an arbitrary `a∈C` into the preceding
subfamily. There is a direct sum of `k[f]`-modules

\[
C=L(C)\oplus k[x,f].
\tag{16}
\]

Existence follows by reducing powers of `g` using

\[
gx^n=\frac{L(x^n)+2nf^3x^{n-1}}{2n+1}\quad(n\ge1),
\qquad g=L(1).
\tag{17}
\]

For uniqueness, if `P` has highest `g`-degree `m`, then `L(P)` has highest
`g`-degree `m+1`, with coefficient `(1+2x∂x)P_m`. This operator is injective
in characteristic zero. A nonzero element of `L(C)` is therefore never
`g`-free.

Write uniquely `a=A₀(x,f)+L(P)`. If `a(0,0,0)=0`, there are fixed points and
no slice. Otherwise that constant, denoted `c`, is nonzero.

### Nonconstant x-dependence in the remainder

Suppose `A₀(x,f)=Σ_{j=0}^d a_j(f)x^j` with `d>0`. Take a formal parameter
`ε`, and provisionally an element `q≠0`. Start the orbit at

\[
(x,y,z,w)=(0,\epsilon,q\epsilon^2,0),\qquad
T=\frac{2}{q\epsilon^5}.
\tag{18}
\]

The first three coordinates at time `T` are `(0,-ε,qε²)`. Throughout the
orbit `f=-ε²`, `g=qε⁶`, and at normalized time `uT`,

\[
x(uT)=\frac4q(u^2-u).
\tag{19}
\]

Polynomial integration gives the average of `A₀` along this path. Equation
(5) gives the average of `L(P)` directly from its endpoints, namely
`gP(0,f,g)`. The complete average is therefore

\[
J(q)=\sum_{j=0}^d\gamma_j a_j(-\epsilon^2)q^{-j}
   +q\epsilon^6P(0,-\epsilon^2,q\epsilon^6),
\quad
\gamma_j=\frac{4^j(-1)^j(j!)^2}{(2j+1)!}.
\tag{20}
\]

All `γ_j` are nonzero. Their formula follows by integration by parts for
`∫₀¹(u²-u)^jdu`, interpreted algebraically.

The polynomial `F(q)=q^dJ(q)` has coefficients in `k[[ε]]`. Its constant
coefficient is nonzero, and its coefficient of `q^d` is the unit
`a₀(-ε²)`, because the second term in (20) starts at degree `d+1`.
Pass to a finite splitting field over `k((ε))` and extend the `ε`-adic
valuation to it, obtaining a valuation ring `V` dominating `k[[ε]]`.[^3]
All orbit identities below are evaluated over its fraction field.
At least one root `ρ` of `F` belongs to `V`.
Indeed, if every root were outside `V`, every reciprocal would be in its
maximal ideal, and the factorization

\[
F(q)=F(0)\prod_i(1-q/\rho_i)
\tag{21}
\]

would place every nonconstant coefficient in that ideal. This contradicts
the unit coefficient of `q^d`. Also `ρ≠0`, since `F(0)≠0`.

Use `q=ρ` in (18). Their first three coordinates are integral because `ρ∈V`;
the equation `J(ρ)=0` makes the fourth displacement zero. Both endpoints thus
lie in `V⁴`. But `qε⁵` is a nonzero element of the maximal ideal,
so the time `T` is not in `V`. The slice identity gives the same contradiction
as (15). This excludes every remainder with `d>0`.

### A nonconstant f-only remainder

Now suppose `A₀=a₀(f)` is nonconstant. Extend scalars to an algebraic closure
and choose a root `α`; it is nonzero because `a₀(0)=c≠0`. On the stable quotient
`f=α`, set `w'=w-rP/α`. Equation (5) gives `D_a(w')=0`. A hypothetical slice
therefore descends further through `w'=0` to a slice of `Δ` on

\[
S_\alpha=k[x,r,g]/(xg-r^2-\alpha^3).
\tag{22}
\]

This is a domain, and its localization at `g` is `k[g±¹,r]` with derivation
`αg∂r`. Its unlocalized kernel is `k[g]`: a genuine Laurent pole cannot
belong to `S_α`, as clearing its minimal denominator and reducing modulo
`g` would make a nonzero scalar vanish.

If a slice existed, the slice theorem would imply `S_α=k[g][s]`. Yet

\[
S_\alpha/(g)=k[x,r]/(r^2+\alpha^3)
\cong k[x]\times k[x]
\tag{23}
\]

over the algebraic closure, whereas `k[g][s]/(g)=k[s]` is a domain. This
contradiction excludes every nonconstant `f`-only remainder.

Only `A₀=c∈k×` remains. Section 4 gives `P∈M`, and Sections 2 and 3 prove
the converse and construct the coordinates. The family theorem follows.

## 6. Examples and checks against false generalizations

| Coefficient a | Outcome | Decisive reason |
| --- | --- | --- |
| `1` | Coordinate slice `w` | Constant coefficient |
| `1+x` | No slice in any degree | Nonconstant canonical remainder |
| `1+f` | No slice in any degree | Nonconstant f-only remainder |
| `1+3fgx-2f⁴` | Slice `w-xr` | Added term is `Δ(xr)` |
| `1+3gx-2f³` | No slice in any degree | `a=1+L(x)`, but `x∉M` |
| `1+5gx²-4f³x` | Slice `w-(x²y+fz)` | `a=1+L(x²)`, and `x²∈M` |
| `1+10x⁴r` | Slice `w+fz+2x²y` | First-pole lemma, `h=x⁵` |

The final row uses the more general first-pole lemma and is not asserted to
be in `C`. The pair of middle examples shows why neither nonconstant
`x`-dependence nor absence of a primitive of the form `rP`, with `P∈C`, is
itself a valid obstruction. Polynomial cancellation of the denominators in
(6) matters.

For `1+3gx-2f³`, an exact rational search found no slice of total degree at
most 16: 4,845 unknown coefficients and 11,758 equations. This finite result
is consistent with, but unnecessary for, the all-degree proof. It is not
being used to justify the theorem.

The independent arithmetic checks in `verify_first_pole.py` cover the new
primitive identities, the cone reduction, fifth-root residue tests, paired
orbit invariants, a cleared zero-displacement certificate, and initial
Hensel coefficients. They also check the exact averaged correction term in
(20) and the monomial and fiber-shear identities. They reuse the standard-library polynomial arithmetic
in `verify_extension.py`, not the research solver. Exact finite identities
do not formalize the quantified proof, valuation-ring existence, or the
general cancellation conjecture. The finite classifier in
`research/primitive_classifier.py` implements both primitive and slice tests;
its positive outputs are substituted into the independently reconstructed
Jacobian derivation. Its test suite includes a 120-monomial decomposition grid
and deliberately incorrect primitives.

From the project directory, reproduce the checks with:

```sh
/opt/anaconda3/bin/python verify_exact.py
python3 verify_extension.py
python3 verify_first_pole.py
/opt/anaconda3/bin/python research/primitive_classifier.py --self-test
/opt/anaconda3/bin/python research/primitive_classifier.py --mode slice --json '1+3*G*X-2*F**3'
/opt/anaconda3/bin/python research/primitive_classifier.py --mode slice --json '1+5*G*X**2-4*F**3*X'
```

The current suites contain 19, 16, 16, and 17 tests respectively, all passing.
The classifier uses exact rational coefficients and SymPy 1.13.3; the theorem
is stated and proved for arbitrary characteristic-zero fields.

## 7. Literature position and the remaining research frontier

The underlying derivation, the slice theorem, and general extension methods
are established literature. Freudenburg's extension results for fundamental
derivations require their stated additional structure; they cannot be applied
to an arbitrary extension simply because it is free.[^4] A statement-level
comparison with the literature is necessary before assigning originality to
the family theorem. No novelty conclusion follows from failing to locate an
identical formula in a targeted search.

The accompanying [statement-level literature audit](research/extension-literature.md)
compares the exact criterion against image, extension, commuting-derivation,
and proper-action results. It records which additional hypotheses prevent
those results from settling arbitrary coefficients. The bounded search found
no exact matching classification in the sources checked; originality still
requires specialist and citation review.

The alternative Koras-Russell cylinder route has a documented limitation.
Boldyrev, Gaifullin, and Shafarevich's December 2024 version explicitly leaves
open whether the modified Derksen invariant distinguishes that cylinder
from affine four-space. Their theorem gives a useful dichotomy for its
nonrigid base: the modified invariant is either the full ring or a proper
infinitely generated algebra.[^5] Computing a proper algebra from selected
slice derivations does not decide which alternative holds for all slices.

For the present derivation, the next precise extension question is now

\[
a\in R\setminus C,\qquad
\Delta+a\partial_w\text{ has a slice}
\quad?\Longrightarrow\quad a\in k^\times+\Delta(R).
\tag{24}
\]

The first-pole lemma handles a further specified portion of that complement,
but not all of it. A second route would generalize the argument to the broader
rank-three constructions in Dasgupta and Gaifullin.[^1] Neither extension
is established here. Even a positive answer to (24) would still require a
separate argument connecting arbitrary four-variable slice derivations to
this construction before it could solve cancellation.

The appropriate present status is: complete family-specific working proof,
exact algebraic checks, originality unestablished, and no expert review or
proof-assistant formalization. The general conjecture remains unresolved
by these results.

## Sources

[^1]: N. Dasgupta and S. Gaifullin, [On locally nilpotent derivations of
    polynomial algebra in three variables](https://arxiv.org/html/2306.00510),
    arXiv version 2, December 9, 2023; published in *Sbornik: Mathematics*
    216:4 (2025), 456–484. Section 5 identifies Freudenburg's explicit
    derivation; Theorem 2.5 states the slice theorem. The family classification
    in this note is not attributed to that paper.

[^2]: The Stacks Project, [Section 59.32: Henselian rings](https://stacks.math.columbia.edu/tag/03QD),
    simple-root lifting and completeness. The particular formal roots used
    here can also be constructed by the coefficient recursion explained
    immediately after equation (12).

[^3]: The Stacks Project, [Section 10.50: Valuation rings](https://stacks.math.columbia.edu/tag/00I8),
    especially Lemma 10.50.2, domination by a valuation ring, and the
    valuation-ring inversion property. Used for the finite algebraic
    splitting-field argument in Section 5.

[^4]: G. Freudenburg, [Actions of SL₂(k) on affine k-domains and fundamental
    pairs](https://arxiv.org/html/2108.12021), arXiv version 2, June 7, 2022,
    Section 7. This is background on extension constructions, not a citation
    claiming the hypotheses or conclusion of its specialized results apply
    to every coefficient considered here.

[^5]: I. Boldyrev, S. Gaifullin, and A. Shafarevich,
    [Modified Derksen invariant](https://arxiv.org/html/2312.08421v2),
    arXiv version 2, December 9, 2024, Introduction and Theorem 1. The
    documented open status belongs to that source version; this note does
    not turn a bounded subsequent search into a proof that no later result
    exists.
