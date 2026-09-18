# Fresh hostile audit of the fixed-Delta classification

September 12, 2026. This is a new model audit of the complete dependency chain, not a human referee report or proof-assistant verification.

## Verdict

I did not find a mathematical counterexample or a missing hypothesis that invalidates the fixed-base classification. I reconstructed the earlier algebraic steps, rather than assuming the higher-pole argument was its only vulnerable part. The arbitrary-characteristic-zero-field statement also survives: the constructive operations remain over the original field, and algebraic extensions are used only to produce contradictions.

One documentation correction was needed in the version of `deep-pass-04.md` read for this audit and has now been applied. Its Section 2 directed the reader to `deep-pass-03.md` for the global kernel and plinth proofs. The explicit proof of the global plinth identity is instead in [lifting-route.md](lifting-route.md), under “The plinth ideal underlying the invariant-coefficient criterion.” The updated main report links that proof and makes the shorter noncircular dependency explicit: the higher-pole argument needs only `f^m∉ΔR`, which follows directly from the independently proved polynomial-primitive criterion in Section 3 of `deep-pass-03.md`.

This audit concerns all coefficients in the single family `Δ+a∂w`. It supplies no reduction of arbitrary slice derivations on four-space to that family and changes nothing about the unresolved global cancellation question.

## Material reconstructed from disk

I read the current main report [deep-pass-04.md](../deep-pass-04.md), the earlier chain in [deep-pass-03.md](../deep-pass-03.md), [extension-normal-forms.md](extension-normal-forms.md), the kernel/plinth/fiber portions of [lifting-route.md](lifting-route.md), and the completed higher-pole and properness proofs in [arbitrary-coefficients-pass.md](arbitrary-coefficients-pass.md). I also inspected the mechanics and stated limits of [full_coefficient_classifier.py](full_coefficient_classifier.py).

Throughout, `k` is a field of characteristic zero,

\[
R=k[x,y,z],\quad f=xz-y^2,\quad
g=zf^2+2x^2yf+x^5,\quad r=-x^3-fy,
\quad\Delta=\operatorname{Jac}(f,g,\cdot).
\]

## 1. Localization is a genuine presentation

The identities `Δr=fg`, `Δx=2fr`, and `r²+f³=xg` were checked against the displayed Jacobian formulas. The nonzero Jacobian `Jac(x,f,g)=2fr` makes `x,f,g` algebraically independent in characteristic zero.

In particular, writing `C=k[x,f,g]` is legitimate. The presentation

\[
R_f\cong C_f[T]/(T^2+f^3-xg)
\]

has the explicit inverse

\[
y=-(T+x^3)/f,\qquad
z=(g+2Tx^2+x^5)/f^2.
\]

Substitution recovers the three defining polynomials `f,g,r`. This uses no inverse of `g`. The quadratic is irreducible over `k(x,f,g)` because `xg-f³` has a simple zero as a rational function in `x` over `k(f,g)`. Consequently the free-module decomposition `R_f=C_f⊕rC_f` has no missing relation or hidden zero divisor.

After additionally inverting `g`, the equation solves for `x` and gives `R_fg=k[f^{±1},g^{±1},r]`, with derivation `fg∂r`. Local nilpotence follows on the original ring because every original polynomial has finite degree in `r` after this injective localization. For arbitrary polynomial `a`, the extension is locally nilpotent too: its successive derivatives of `w` are `a,Δa,Δ²a,...`.

## 2. The canonical direct sum is correct

Use independent formal variables `X,F,G` for this check and set

\[
L(P)=GP+2(XG-F^3)P_X.
\]

For a monomial,

\[
L(X^nG^bF^c)
=(2n+1)X^nG^{b+1}F^c-2nX^{n-1}G^bF^{c+3}.
\]

This yields a terminating reduction in the `G` exponent. The remainder of `X^nG^bF^c` in the proposed complement is explicitly

\[
\pi(X^nG^bF^c)=
\begin{cases}
F^{c+3b}X^{n-b}\displaystyle\prod_{j=0}^{b-1}
\frac{2(n-j)}{2(n-j)+1},&b\le n,\\
0,&b>n.
\end{cases}
\]

The proof includes the boundary case `n=0`: then `G=L(1)`, so the remainder really vanishes rather than generating a negative power of `X`.

For uniqueness, if `P=Σ_{j=0}^mP_j(X,F)G^j` with `P_m≠0`, the coefficient of `G^{m+1}` in `L(P)` is `(1+2X∂X)P_m`. This is nonzero because it multiplies the `X^i` coefficient by `2i+1`. Hence a nonzero `L(P)` cannot be `G`-free. This establishes

\[
C=L(C)\oplus k[x,f]
\]

as `k[f]`-modules. It is not a claim that `L(C)` is an ideal. The same proof works with Laurent coefficients in `f`, justifying localization of the direct sum.

An independently written recursion, separate from the existing classifier, checked this identity and the closed remainder formula for all `0≤n,b≤7` and `-2≤c≤2`: 320 monomials. All checks passed. The negative `c` values specifically test the localized statement.

## 3. The primitive-image argument has the needed intersection property

For `ΔH=a∈C`, the decomposition `H=U+rV` in `R_f` gives

\[
\Delta H=2frU_x+fL(V).
\]

Uniqueness of the `1,r` decomposition implies `U_x=0`, so `U∈k[f^{±1},g]`. Put `P=fV`. The inverse recursion for `L(P)=a` gives coefficients only in `k[f,g^{±1}]`; the same `P` already belongs to `C_f`. Their intersection is `C`, because `f,g` are independent prime variables. Thus no genuine `g` denominator can be concealed in the odd part of a polynomial primitive.

The remaining invariant term has at most one `f` denominator. A higher minimal denominator would, after multiplication and reduction modulo `f`, make a nonzero polynomial in `g=x⁵` vanish. This cannot happen. Reducing the numerator of `H=(rP+Q)/f` then gives exactly

\[
x^3P(x,0,x^5)\in k[x^5].
\]

The congruence condition on exponents is therefore correct, as is the module

\[
M=(f,g-x^5)C+x^2k[f,g].
\]

In particular, `L^{-1}(f^m)=f^m/g` has a genuine `g` denominator. This proves `f^m∉ΔR` without invoking either the extension classification or its higher-pole step. Thus the degree-bound dependency is not circular.

## 4. Kernel and special-fiber assertions survive direct reconstruction

The global kernel is obtained by intersecting `k[f^{±1},g^{±1}]` with `R`. Negative `f` powers are excluded by clearing denominators and reducing modulo `f`, where `g=x⁵` remains transcendental over `k`. Once those denominators are removed, negative `g` powers are excluded on the line `x=z=0`, where `g=0` and `f=-y²` remains transcendental. This gives `kerΔ=k[f,g]`.

For `α≠0`, the fiber has the actual presentation

\[
R/(f-\alpha)\cong
k[x,r,g]/(xg-r^2-\alpha^3),
\qquad \Delta r=\alpha g,\quad\Delta x=2\alpha r.
\]

The polynomial defining it is primitive and linear in `x` over `k[r,g]`, so the ring is a domain. After inverting `g`, its kernel is `k[g^{±1}]`. A minimal negative `g` denominator is impossible because the quotient by `g` is nonzero. Thus the unlocalized kernel is exactly `k[g]`.

The contradiction from its `g=0` fiber must be taken after extending the field if necessary: `r²+α³` then has two distinct roots because `α≠0` and the characteristic is zero. Over a nonsplitting original field it might be irreducible, so “the fiber has zero divisors over every field” would be wrong. The current proofs correctly permit the algebraic-closure extension.

For the auxiliary `g=d≠0` fiber, the proof does not assume `g-d` irreducible. Since `f` is irreducible and does not divide `g-d`, multiplication by `f` in `R/(g-d)` is injective. Its `f` localization is `k[f^{±1},r]`, a domain, hence the original quotient embeds into a domain. Its kernel is `k[f]`; the `f=0` fiber splits into five lines over an algebraic closure. This validates the separate plinth calculation. None of these fiber arguments presupposes the classification they support.

Independent symbolic substitution checked both inverse fiber presentations and the three localization identities, with zero residuals.

## 5. The first-pole certificate really excludes arbitrary slices

On the cone `R/(f)`, localizing at `x` gives `k[x^{±1},y]` and the derivation `5x⁵∂y`. Intersecting its kernel back with the cone yields exactly `k[x]`. Therefore `f|ΔH` really does imply `H=h(x)+fK`, rather than merely a rational residue.

If `h∉k[x⁵]`, a primitive fifth root `ζ` makes `h(ζB)-h(B)` nonzero. The polynomial

\[
c(1-\zeta^3)+B^2(h(\zeta B)-h(B))
\]

has positive degree and nonzero constant, so its root `b` can be chosen nonzero over an algebraic closure. The two roots of `X⁶-b⁵X+ε³` near `b,ζb` are simple: their derivative is `5b⁵`, not zero. The associated endpoints have invariant values `f=ε,g=b⁵`, and time with residue numerator `b³(1-ζ³)≠0`.

The selected equation makes the fourth-coordinate displacement integral. It need not make that displacement zero. This is sufficient: evaluation of any polynomial slice at the two integral endpoints would give an integral difference equal to a time with a pole. There is no bounded-degree assumption on the hypothetical slice.

If `h∈k[x⁵]`, subtracting the corresponding polynomial in `g` and dividing by `f` is an actual polynomial operation. This checks both directions of the criterion and its signs.

## 6. The arbitrary-coefficient reduction does not assume integral localized terms

For arbitrary `a∈R`, write `a=A_0(x,f)+ΔK/f` with `K∈R_f`. The symmetric-orbit average is integral in `e` because it is the original polynomial `a` evaluated on the explicitly integral Laurent-polynomial trajectory. Its separate normal-form summands need not be integral before collection.

The negative `Q` powers are precisely the positive-`x` terms of `A_0`. The `L(P)` correction averages to `gP(0,f,g)`, containing only positive powers of `Q`; the `rB` term averages to zero. Thus the coefficient separation used in the argument is valid even with `f` denominators.

The root argument requires a nonzero constant coefficient and a unit coefficient in the cleared polynomial. It does **not** require its constant coefficient to be a unit. If all roots had negative valuation, every reciprocal root would have positive valuation and every nonconstant coefficient would be nonunit, contradicting the specified unit coefficient. This proves the existence of the integral root used for the pole-time certificate.

The surviving constant-in-`x` Laurent polynomial must actually be in `k[f]`, since its substitution at `f=-e²` is the constant-in-`Q` coefficient of an element of `k[e,Q,Q^{-1}]`. A nonconstant remainder is then ruled out on a nonzero `f` fiber using the independently checked kernel calculation above.

## 7. Higher poles and properness were rechecked in their full context

The low-degree removal is valid because `Δ` raises homogeneous degree by four and `f^m∉ΔR`. Subtracting invariant homogeneous components changes the residue only by powers of `x⁵`, so it cannot erase the nonremovable residue.

For the fixed-`g` formal branches, every corrected monomial has exponents `L=l-6n`, `J=j+3n`, preserving `L+2J=D`. This is the essential correction to the earlier raw-monomial attempt. The nonzero `J=0` branch difference ensures the finite edge set is nonempty. The strict degree bound ensures each selected slope exceeds two. The high-`J` terms then have strictly larger valuation, and the edge has a nonzero lower-degree term as well as the nonzero leading `V^{m-1}` term.

At a potentially repeated nonzero root, formal Weierstrass preparation applies over the complete DVR coefficient ring. The distinguished polynomial's roots have positive valuation: they are integral by monicity, and their reduction satisfies a pure power equation. Evaluation of the resulting series is legitimate in a finite complete valued extension. The endpoint coordinates are integral and the exact time has valuation `-M-2N`. This gives the required contradiction without assuming that the leading root is simple.

The properness strengthening uses these same pairs in the valuative criterion for the action morphism. The remaining nonconstant-`f` case has the separate exact time `2v/G` on the invariant fiber. Restriction to a closed invariant fiber is a base change of that action morphism. Thus the properness argument has no extra hidden descent or freeness assumption.

## 8. Positive coordinates and field descent

For `a=c+ΔH`, the change `s=(w-H)/c` is a polynomial coordinate change over `k`. In the new ring `k[x,y,z,s]`, extend `Δ` by `Δs=0`. Then `-sΔ` is locally nilpotent and

\[
\alpha=\exp(-s\Delta)
\]

is a polynomial automorphism with inverse `exp(sΔ)`. Its three base coordinates are killed by `Δ+∂s`, and its fourth coordinate is `s`. Thus its invariant ring is exactly the polynomial ring generated by those three coordinates. This avoids interpreting a variable-time substitution as an automorphism without proof.

There is no unresolved Galois-descent step. A slice over `k` gives the fixed-line constant `c∈k*`. Canonical decompositions and denominator clearing use coefficients in `k`. Whenever a residue belongs to `k[x⁵]`, its matching polynomial `P(g)` already has coefficients in `k`; repeated pole removal therefore constructs the primitive over `k`. Nonexistence arguments may freely extend constants, since an existing slice would survive. The argument never concludes “there is a primitive over the closure, therefore it is over k” without justification.

## Finite checks run during this audit

In addition to the separately written 320-monomial decomposition test and inverse-presentation checks, I reran:

- `python3 verify_first_pole.py`: 16 test methods passed.
- `python3 verify_higher_poles.py`: 9 test methods passed.
- `/opt/anaconda3/bin/python research/full_coefficient_classifier.py --self-test`: 9 test methods passed.

These finite checks support the formulas and implementation. They do not establish the quantified theorem by themselves. The present audit found no defect in the mathematical chain, but it is still model-based verification of a private working proof, with originality and expert review unresolved.
