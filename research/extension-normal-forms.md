# Polynomial primitives in the extended coefficient family

Let `k` have characteristic zero and retain

\[
f=xz-y^2,\qquad g=zf^2+2x^2yf+x^5,\qquad r=-x^3-fy,
\]

with `R=k[x,y,z]` and `Delta=Jac(f,g,.)`. Put

\[
A=k[f,g],\quad C=k[x,f,g],\quad
L(P)=gP+2(xg-f^3)\frac{\partial P}{\partial x}.
\]

Here `x,f,g` are algebraically independent: their Jacobian is `Delta x=2fr≠0`, so their differentials are independent over the fraction field in characteristic zero. Thus `C` is a polynomial ring, and the derivative in `L` fixes `f,g`. The identities `Delta r=fg` and `r²+f³=xg` give

\[
\Delta(rP)=fL(P),\qquad P\in C.
\]

This note determines exactly which elements of `C` have a polynomial primitive under `Delta`. It then gives an all-degree slice classification for every coefficient in `C`: a slice exists exactly when the coefficient is a nonzero constant plus a polynomial `Delta`-derivative. The final reduction also makes the classification a finite exact test. These results are not claimed to be new in the literature.

## Why primitives of the form `rP` are insufficient

Define the actual polynomials

\[
t=2x^2y+fz=\frac{g-x^5}{f},\qquad
S=x^2y+fz=\frac{rx^2+g}{f}.
\]

Although their displayed fractions have denominators, both numerators are divisible by `f` in `R`. In particular,

\[
\Delta S=5gx^2-4f^3x=L(x^2).
\]

This is not divisible by `f` in `C`. Every `Delta(rP)` with `P∈C` is divisible by `f`, so the image `Delta(R)∩C` is strictly larger than the image of `rC` under `Delta`.

For example, `Delta+(1+5gx²-4f³x)∂w` has the explicit slice `w-S`. The canceled denominator is a real polynomial identity, not permission to use a rational coordinate change as a polynomial one.

## An exact description of the primitive image

Set

\[
M=(f,g-x^5)C+x^2A\subset C.
\]

This is an `A`-submodule; its notation is a sum of submodules, not an assertion that `x²A` is an ideal of `C`.

**Proposition.** One has

\[
\Delta(R)\cap C=L(M).
\]

For

\[
P=fP_1+(g-x^5)P_2+x^2Q,
\qquad P_1,P_2\in C,\quad Q\in A,
\]

an explicit polynomial primitive of `L(P)` is

\[
H=rP_1+rtP_2+QS.
\]

**Proof of sufficiency.** The formulas defining `t,S` give

\[
H=\frac{rP+gQ}{f}
\]

in the fraction field, and the first expression proves that it belongs to `R`. Since `gQ` is invariant, differentiating gives `Delta H=L(P)`.

**Proof of necessity.** Let `a∈C` and suppose `Delta H=a` for some `H∈R`. After inverting `f`, equations for `y,z` give

\[
R_f=C_f[r]/(r^2+f^3-xg).
\]

This is a free `C_f`-module with basis `1,r`. To justify that there is no further relation, the polynomial `xg-f³` is not a square in `k(x,f,g)`: as a rational function in `x` over `k(f,g)` it has a simple zero. Thus the quadratic has degree two over that field. Equivalently, the explicit formulas for `y,z` and the defining relation provide inverse maps.

Write uniquely `H=U+rV`, with `U,V∈C_f`. The odd and even parts of its derivative are

\[
\Delta H=2frU_x+fL(V).
\]

Since `a∈C` has no `r` component, `U_x=0`; characteristic zero gives `U∈A_f`. Put `P=fV`, so `L(P)=a`.

Let `K=k(f,g)`. The map `L:K[x]→K[x]` is invertible: it preserves polynomial degree, with leading multiplier `(2d+1)g` in degree `d`. More explicitly, if `a=Σ_{j=0}^d a_jx^j` and `P=Σ p_jx^j`, its unique inverse is given by

\[
p_d=\frac{a_d}{(2d+1)g},\qquad
p_j=\frac{a_j+2(j+1)f^3p_{j+1}}{(2j+1)g}
\quad(j=d-1,\ldots,0).
\]

Every `p_j` therefore lies in `A[g^-1]`. On the other hand, `P=fV∈C_f`. The intersection of these two coefficient rings is `C`, because `f,g` are distinct polynomial variables. Hence `P∈C`.

We now know

\[
H=\frac{rP}{f}+U,\qquad U\in A_f.
\]

The invariant term `U` cannot have a pole of order greater than one in `f`. If it had minimal denominator `f^m`, `m>1`, multiplying by `f^m` and reducing modulo `f` in `R` would make a nonzero polynomial in `g` vanish. That is impossible: modulo `f`, `g=x⁵`, so `k[g]` injects into `R/(f)`. Thus `U=Q_0(f,g)/f` for some `Q_0∈A`, with regular invariant terms absorbed into `Q_0`.

Polynomiality of `H` is exactly divisibility of `rP+Q_0` by `f` in `R`. Reducing modulo `f` gives `r=-x³`, `g=x⁵`, and hence

\[
x^3P(x,0,x^5)=Q_0(0,x^5)\in k[x^5].
\]

This condition is equivalent to `P(x,0,x⁵)∈x²k[x⁵]`: the monomial exponents of a polynomial multiplied by `x³` must all be divisible by five. Since the kernel of `C→k[x]`, `(x,f,g)↦(x,0,x⁵)`, is `(f,g-x⁵)`, this says exactly `P∈M`. Necessity follows. ∎

The proposition is an effective finite test for a specified coefficient `a`. Compute the unique `P=L^-1(a)` by the displayed recursion. Reject a polynomial primitive if any genuine denominator in `g` remains. Otherwise evaluate `P(x,0,x⁵)` and check whether all its nonzero monomials have exponent congruent to `2` modulo `5`. A successful test gives the displayed polynomial primitive. No search over arbitrarily high primitive degree remains for this fixed question.

## A slice classification within `c+L(C)`

**Proposition.** Let `c∈k*` and `P∈C`. For

\[
D=\Delta+\bigl(c+L(P)\bigr)\partial_w,
\]

there is a polynomial slice if and only if `P∈M`. In the positive case a slice is `(w-H)/c`, with `H` as above.

The positive direction follows from the primitive proposition. Its converse requires an all-degree obstruction; absence of a polynomial primitive alone would not prove absence of a nonlinear slice.

**Proof of necessity.** Suppose `P∉M` and set

\[
H=rP\in R,\qquad
h(X)=-X^3P(X,0,X^5)\in k[X].
\]

The residue of `H` modulo `f` is `h(x)`, and `P∉M` says `h∉k[X⁵]`. Over an algebraic closure, choose a primitive fifth root of unity `zeta`. Then `h(zeta X)-h(X)` is nonzero. The polynomial

\[
c(1-\zeta^3)+X^2\bigl(h(\zeta X)-h(X)\bigr)
\]

has positive degree and a nonzero constant term, so it has a root `b≠0`. Set `d=b⁵`.

Work with a formal parameter `epsilon`. The polynomial equation

\[
X^6-dX+\epsilon^3=0
\]

has unique formal solutions `x1(epsilon),x2(epsilon)` with constant terms `b,zeta b`. Existence follows directly by recursive coefficient comparison: the derivative in `X` at each constant root is `5d≠0`, so the next unknown coefficient occurs with a nonzero constant multiplier. Thus both solutions are units of the formal power-series ring.

The two triples

\[
p_i=(x_i,0,\epsilon/x_i)
\]

have `f=epsilon`, `g=d`, and `r_i=-x_i³`. Set

\[
T=\frac{r_2-r_1}{\epsilon d}.
\]

Its numerator has nonzero constant term `b³(1-zeta³)`, so `T` has a pole. The `Delta` flow at time `T` joins `p1` to `p2`: it sends `r1` to `r2`, then `x=(r²+f³)/g` fixes the required final `x`, and the formulas for `y,z` fix the remaining coordinates.

Since `Delta H=fL(P)`, the fourth-coordinate displacement for `D` is

\[
W=cT+\frac{H(p_2)-H(p_1)}\epsilon
=\frac{c(r_2-r_1)/d+H(p_2)-H(p_1)}\epsilon.
\]

The numerator has zero constant term by the equation defining `b`. Therefore `W` belongs to the formal power-series ring. The full `D` flow joins the two integral points `(p1,0)` and `(p2,W)` at the nonintegral time `T`.

A polynomial slice would satisfy `s(p2,W)-s(p1,0)=T`. Its left side is a power series with no pole; its right side has a pole. This contradiction excludes every polynomial slice. As usual, a slice over the original field would survive extension to the field containing the chosen constants, so the conclusion holds over `k`. ∎

For this subclass, the distinction is therefore exact: `c+L(P)` admits a slice precisely when `c+L(P)` differs from a nonzero constant by an actual polynomial `Delta`-derivative. The remaining coefficients in `C` are handled by the reduction below.

## A more general theorem for a rational primitive with one `f` denominator

The preceding pole argument applies to every polynomial `H∈R` with `f` dividing `Delta H`, not only to `H=rP`.

**Theorem.** Let `c∈k*`, let `H∈R`, and suppose `f|Delta H`. There is a unique polynomial `h(x)∈k[x]` representing the residue of `H` modulo `f`. Then

\[
\Delta+\left(c+\frac{\Delta H}{f}\right)\partial_w
\text{ has a polynomial slice}
\quad\Longleftrightarrow\quad h(x)\in k[x^5].
\]

Here the existence of a residue polynomial in `x` is part of the theorem's proof, not an additional assumption. All the displayed actions are fixed-point-free.

To establish the residue statement, reduce `Delta` on the domain `R/(f)=k[x,y,z]/(xz-y²)`. After inverting `x`, the ring is `k[x,x^-1,y]` and the derivation is `5x⁵∂y`. Its kernel is `k[x,x^-1]`; a genuine Laurent pole in `x` cannot belong to the original ring because clearing the smallest denominator and reducing modulo `x` would make a nonzero scalar vanish. Thus the kernel before localization is exactly `k[x]`. Since `f|Delta H`, the residue of `H` belongs to that kernel, giving

\[
H=h(x)+fK\qquad(K\in R).
\]

If `h(x)=P(x⁵)`, then `g≡x⁵ mod f` gives `H-P(g)=fK'` for a polynomial `K'`. Consequently `Delta H/f=Delta K'`, and `(w-K')/c` is a polynomial slice.

If `h∉k[x⁵]`, use precisely the formal construction in the preceding proof: choose `zeta,b,d`, lift the two roots of `X⁶-dX+epsilon³`, and set `p_i=(x_i,0,epsilon/x_i)`. The residue of the arbitrary polynomial `H` at these two points is still `h(b)` and `h(zeta b)`. Hence the same defining equation for `b` makes

\[
W=\frac{c(r_2-r_1)/d+H(p_2)-H(p_1)}\epsilon
\]

integral, while `T=(r2-r1)/(epsilon d)` has a pole. The flow identity and slice contradiction are unchanged. This proves necessity in every polynomial degree.

There is a particularly simple form of the theorem. From `H=h(x)+fK` and `Delta x=2fr`,

\[
\frac{\Delta H}{f}=2rh'(x)+\Delta K.
\]

The polynomial shear `w'=w-K` therefore turns the action into

\[
\Delta+\bigl(c+2rh'(x)\bigr)\partial_{w'}.
\]

For any `h∈k[x]`, this action has a slice exactly when `h∈k[x⁵]`. Its coefficient equals `c` on the fixed line `x=y=0`, where `r=0`, so every such action is fixed-point-free. The shear preserves that property. This proves the fixed-point assertion without requiring a separate ideal-theoretic argument.

This theorem by itself does not classify arbitrary coefficients in `R` or in `C`. Its hypothesis is the specific representation `c+Delta H/f` with `H` polynomial and `Delta H` divisible by `f`. The following complementary-case argument completes the classification in `C`.

## The coefficient `1+3gx-2f³`

Here `a=1+L(x)`. The unique normal-form polynomial is `P=x`, which fails the congruence test: its exponent is `1`, not `2`, modulo five. Thus it has no polynomial primitive after subtraction of the constant, and the preceding slice proposition proves that it has no slice at all.

There is also a compact exact orbit certificate with zero fourth-coordinate displacement. Let `zeta` be a primitive fifth root of unity and take a parameter `v` near `zeta`. Write `S_j(v)=1+v+...+v^j`. In a finite algebraic extension of `k(zeta)(v)`, choose elements `b,F` satisfying

\[
b^6=-\frac{S_2}{S_5S_3},\qquad
F^3=b^6vS_4.
\]

Choose a valuation ring dominating `k(zeta)[v]_(v-zeta)`. At `v=zeta`, `S4=0`, `S5=1`, and `S2,S3` are nonzero. Hence `b` and `v` are units, while `F` has positive valuation. The points

\[
P=(b,0,F/b,0),\qquad
Q=(bv,0,F/(bv),0)
\]

are integral and have common invariants `f=F`, `g=b⁵S5`. Their time difference is

\[
T=\frac{b^3(1-v^3)}{Fg},
\]

which has a pole. Because `a=1+Delta(xr)/f`, the fourth-coordinate displacement is

\[
T+\frac{b^4(1-v^4)}F
=\frac{1-v}{Fb^2S_5}\bigl(S_2+b^6S_5S_3\bigr)=0.
\]

A polynomial slice would equate its integral endpoint difference with the nonintegral time `T`. This independently excludes a slice for the same coefficient. The valuation-ring existence used here is the domination lemma cited in the companion lifting note.

## Completing the classification for all coefficients in `C`

There is a direct sum of `k[f]`-modules

\[
C=k[x,f]\oplus L(C).
\]

For existence, eliminate every positive power of `g` using

\[
gx^n=\frac{L(x^n)}{2n+1}
+\frac{2n}{2n+1}f^3x^{n-1}\quad(n\ge1),\qquad g=L(1).
\]

Multiplying this identity by powers of `g` and `f` decreases the `g` exponent of the remainder and terminates. For directness, if `P` has highest `g` degree `m`, the highest `g` degree of `L(P)` is `m+1`, with coefficient `(1+2x∂x)P_m`. That coefficient is nonzero because this operator multiplies the coefficient of `x^j` by `2j+1`. Hence a nonzero element of `L(C)` cannot belong to `k[x,f]`.

Write the resulting unique decomposition as

\[
a=A(x,f)+L(P),\qquad P\in C,\quad A\in k[x,f].
\]

The action has fixed points if `c=a(0,0,0)=A(0,0)=0`, so assume `c≠0`. Suppose first that `d=deg_x A>0`, and write `A=Σ_{j=0}^d a_j(f)x^j`. Define

\[
\kappa_j=\frac{4^j(j!)^2}{(2j+1)!}.
\]

Use the symmetric orbit from the companion note, starting at `(0,e,qe²,0)` with `f=-e²`, `g=qe⁶`, and time `T=2/(qe⁵)`. The average of the `A` term along this orbit is

\[
\sum_{j=0}^d\kappa_j a_j(-e^2)(-1/q)^j.
\]

For the other term, `Delta(rP)=fL(P)`. Both endpoints have `x=0`, and their `r` difference is `fgT`. Consequently the average of `L(P)` is exactly `gP(0,f,g)`. Thus the full average coefficient is

\[
J(q)=\sum_{j=0}^d\kappa_j a_j(-e^2)(-1/q)^j
+qe^6P(0,-e^2,qe^6).
\]

The expression `F(q)=q^dJ(q)` is a polynomial over `k[[e]]`. Its constant coefficient is the nonzero integral element `(-1)^d kappa_d a_d(-e²)`. Its coefficient of `q^d` is the unit `a_0(-e²)`, because the added `P` term starts in degree `d+1`. The substitution `f↦-e²` is injective, so no nonzero leading coefficient disappears.

Choose a splitting field of `F` over `k((e))` and a valuation ring `V` dominating `k[[e]]`. At least one root `q` lies in `V`. Indeed, otherwise every root `rho` would have reciprocal in the maximal ideal, and

\[
F(q)=F(0)\prod_\rho(1-q/\rho)
\]

would force every nonconstant coefficient into that ideal, since `F(0)` is integral. This contradicts the unit coefficient in degree `d`. Every root is nonzero because `F(0)≠0`.

For such a nonzero integral root `q`, the full fourth-coordinate displacement is `T J(q)=0`. The two endpoints `(0,±e,qe²,0)` are integral, but `T=2/(qe⁵)` has a pole. A polynomial slice would equate an integral endpoint difference with this nonintegral time. Therefore `d>0` is impossible when a slice exists.

Suppose next that `A=a(f)` is nonconstant. Since `a(0)=c≠0`, choose a nonzero root `alpha` after scalar extension. On the invariant quotient `f=alpha`, the polynomial shear

\[
w'=w-rP/\alpha
\]

makes `w'` invariant, because the coefficient becomes `a(alpha)=0`. A slice would then descend under `w'=0` to one on the surface with equation `xg=r²+alpha³` and derivation `Delta r=alpha g`, `Delta x=2alpha r`. Its kernel is `k[g]`, and its `g=0` fiber is a union of two distinct affine lines over the algebraic closure, contradicting the slice theorem. The detailed domain and kernel argument appears in the companion lifting note.

The canonical remainder of any slice coefficient must therefore be the nonzero constant `A=c`. The earlier first-pole result then says that the correction `P` must belong to `M`. Conversely, `P∈M` provides a polynomial primitive `H` and the explicit slice `(w-H)/c`.

We have proved, for every `a∈C`,

\[
D_a\text{ has a polynomial slice}
\Longleftrightarrow
a=c+L(P),\ c\in k^*,\ P\in M
\Longleftrightarrow
a=c+\Delta H,\ c\in k^*,\ H\in R.
\]

Every positive case has an explicit polynomial kernel: use the shear `w'=w-H`, then the finite `Delta` flow with independent parameter evaluated at `-w'/c` to obtain three invariant coordinates. Its inverse uses the opposite flow and the inverse shear. The proof therefore excludes an exotic polynomial kernel throughout this entire coefficient family.

## Finite exact implementation and remaining scope

The companion `primitive_classifier.py` implements `L^-1`, the module test, actual polynomial primitive construction, and the canonical direct-sum reduction. It reconstructs the Jacobian derivation independently and verifies every returned primitive by exact differentiation in `k[x,y,z]`. Its separate slice mode applies only to the specific extension family proved here. The default primitive mode does not identify absence of a primitive with absence of a slice.

These propositions classify all coefficients in `k[x,f,g]` for this particular `Delta`. They do not classify all coefficients in `k[x,y,z]`, all four-variable locally nilpotent derivations, or the general cancellation problem. The canceled denominators in `S` and `t` explain why the smaller `rP` ansatz missed valid positive cases. No novelty claim is established.
