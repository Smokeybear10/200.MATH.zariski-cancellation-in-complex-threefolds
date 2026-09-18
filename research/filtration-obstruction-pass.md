# Lower coefficients do not repair top-symbol rank automatically

This bounded pass studies the proposed global route from
`B=K[s]≅C[x₁,x₂,x₃,x₄]`, with `E=∂s`, to enough intrinsic locally nilpotent derivations on `K`. The examples below have `K=C[a,b,c]` already polynomial. They are exact negative controls for inference rules, not cancellation counterexamples.

The outcome is precise: lower coefficient extraction, commutation with `E`, and projection to `s=0` all fail to preserve local nilpotence in general. The failure occurs even for genuine ambient coordinate partial derivatives. One example has common top-symbol rank one and a problematic coordinate partial that fixes `s`.

## 1. What the filtration really guarantees

For a derivation `T` of `K[s]`, write

\[
T|_K=\sum_{j=0}^q s^j\delta_j,
\qquad T(s)=h(s),
\]

where each `δ_j` is a derivation of `K`. Suppose `T` is locally nilpotent and its restriction to `K` is nonzero. The highest homogeneous derivation for the `s`-degree filtration is locally nilpotent. Its value on `s` cannot be a nonzero multiple of `s`: for an LND on a characteristic-zero domain, `D(u)∈uB` implies `D(u)=0`. One proof uses `deg_D(Du)=deg_D(u)-1` and `deg_D(uv)=deg_D(u)+deg_D(v)`.

Consequently `deg_s h≤q`, and the highest symbol is `s^qδ_q`, with `δ_q` locally nilpotent on `K`. Commuting ambient coordinate partials have commuting intrinsic top derivations. A purely vertical derivation can instead have filtration degree `-1` and produce no intrinsic derivation.

Repeated commutation has the exact formula

\[
\operatorname{ad}_E^j(T)=\partial_s^j(T)
\]

on its coefficient functions. In particular,

\[
\operatorname{ad}_E^q(T)=q!\bigl(\delta_q+h_q\partial_s\bigr),
\]

which is locally nilpotent and restricts to the already known `q!δ_q`. Thus the highest nonzero repeated commutator recovers the top intrinsic direction; it does not by itself repair rank loss. Intermediate commutators and coefficients require separate verification, as the examples show.

If three commuting intrinsic LNDs on the affine threefold `Spec K` have generic rank three, their `G_a³` action has an open orbit. Unipotent-group orbits on affine varieties are closed, so this orbit is the whole irreducible variety. The stabilizer is zero-dimensional and hence trivial for `G_a³` in characteristic zero; the homogeneous space is `A³`. No factoriality or extension-across-a-boundary argument is needed. The closed-orbit theorem is stated as [Milne, *Algebraic Groups*, Theorem 17.64](https://www.jmilne.org/math/Books/iAG2022.pdf).

## 2. A coordinate partial with a non-nilpotent coefficient

On `C[a,b,c,s]`, take the polynomial coordinates

\[
u=a+s^2,\qquad v=s+u^2,\qquad b,\ c.
\]

Their inverse is `s=v-u²`, `a=u-(v-u²)²`, with `b,c` unchanged. The coordinate partial `T=∂u`, holding `v,b,c` fixed, is

\[
T=(1+4as+4s^3)\partial_a-2(a+s^2)\partial_s.
\]

It is locally nilpotent because it is an actual polynomial coordinate partial. Its top symbol is `4s³∂a`. Its horizontal coefficient of `s¹`, however, is

\[
\delta_1=4a\partial_a,
\qquad\delta_1^n(a)=4^n a\ne0\quad(n\ge1).
\]

The coefficient is not locally nilpotent. Also

\[
[E,T]=(4a+12s^2)\partial_a-4s\partial_s,
\qquad [E,T]^n(s)=(-4)^n s\ne0.
\]

Thus even the first commutator of two ambient LNDs need not be an LND.

## 3. The same failure with common top rank one and `T(s)=0`

Let

\[
N(s)=\begin{pmatrix}s&-s^2\\1&-s\end{pmatrix},
\qquad N(s)^2=0,
\]

and define

\[
A=a-c(sa-s^2b),\qquad
B=b-c(a-sb).
\]

Then `(A,B,c,s)` is a polynomial coordinate system. In matrix form,

\[
\binom A B=(I-cN(s))\binom a b,
\qquad
\binom a b=(I+cN(s))\binom A B.
\]

The inverse identity follows from `N²=0`, and both directions were checked by direct substitution.

The coordinate partial in the `c` direction is

\[
T_c=\partial_c+(sa-s^2b)\partial_a+(a-sb)\partial_b,
\qquad T_c(s)=0.
\]

Its coefficients are

\[
\delta_0=\partial_c+a\partial_b,\qquad
\delta_1=a\partial_a-b\partial_b,\qquad
\delta_2=-b\partial_a.
\]

The middle coefficient is not locally nilpotent, since `δ₁(a)=a`. The commutator

\[
[E,T_c]=(a-2sb)\partial_a-b\partial_b
\]

also fixes `s` but is not locally nilpotent, since it sends `b` to `-b`. The bad commutator is therefore not explained merely by a nonzero vertical component.

The other coordinate partials are

\[
\begin{aligned}
T_A&=(1+cs)\partial_a+c\partial_b,\\
T_B&=-cs^2\partial_a+(1-cs)\partial_b,\\
T_s&=\partial_s+
(ca-2csb+c^2sa-c^2s^2b)\partial_a\\
&\hspace{38mm}+(-cb+c^2a-c^2sb)\partial_b.
\end{aligned}
\]

Their top symbols and intrinsic directions are:

| Coordinate partial | Top symbol | Intrinsic LND |
| --- | --- | --- |
| `T_A` | `cs∂a` | `c∂a` |
| `T_B` | `-cs²∂a` | `-c∂a` |
| `T_c` | `-bs²∂a` | `-b∂a` |
| `T_s` | `-c²bs²∂a` | `-c²b∂a` |

All four ambient coordinate partials commute, but their intrinsic top directions have rank only one over `Frac K`. The non-LND lower coefficient and commutator occur within precisely this degeneracy.

Even locally nilpotent coefficients need not commute: `δ₀` and `δ₂` above are LNDs, but

\[
[\delta_0,\delta_2]=-a\partial_a+b\partial_b=-\delta_1.
\]

Hence a repair must check both local nilpotence and compatibility of the selected directions.

This example does not show that every repair fails. Here `T_A,T_B,T_c` all fix `s`, so they descend to the quotient by `(s)`. Their descended constant terms

\[
\partial_a+c\partial_b,\qquad
\partial_b,\qquad
\partial_c+a\partial_b
\]

are commuting LNDs of rank three. The successful descent uses the extra condition that these ambient derivations preserve `(s)`. Arbitrary ambient coordinate partials need not satisfy it. The example refutes automatic preservation for interior coefficients, not all possible coordinate changes or selection procedures.

## 4. Subtracting the vertical part and projecting can also fail

Take instead

\[
u=s+a^2,\qquad v=a+u^2,
\]

with `b,c` unchanged. The inverse is

\[
a=v-u^2,\qquad s=u-(v-u^2)^2.
\]

For the coordinate partial `T=∂u`,

\[
T(a)=-2(s+a^2),\qquad
T(s)=1+4a(s+a^2).
\]

Let `π:K[s]→K` be the slice projection `s↦0`. Either extracting the constant horizontal coefficient or first replacing `T` by `T-T(s)E` and then projecting gives

\[
\delta=\pi\circ T|_K=-2a^2\partial_a.
\]

An induction gives

\[
\delta^n(a)=(-2)^n n!a^{n+1}\ne0\quad(n\ge1).
\]

Thus the projected derivation is not locally nilpotent. Although `T-T(s)E` fixes `s`, the subtraction itself is not a local-nilpotence-preserving operation. This closes the proposed shortcut of removing the vertical part before evaluating.

## 5. Exact checks and the remaining question

The added checks in [verify_global_filtration.py](../verify_global_filtration.py) validate both polynomial inverse compositions, coordinate-partial pairing, the explicit coefficients and brackets, and all displayed top ranks. The total suite now has **19 passing test methods**. The non-nilpotence claims use the exact recurrences proved above, not a finite failure to reach zero.

The suite also contains a nonlinear modification of the original rank-one chain: `(a+s²,b+as,c+bs,s+(a+s²)²)`. Its inverse is explicit, its four top symbols again have rank one, and its lower coefficient `4a∂a-∂b-2a²∂c` is not locally nilpotent. A separate test exhibits a successful choice of other coefficients in that example, guarding against overstating the negative result.

An additional control from the parallel audit starts with `(a,b+a²s,c+bs,s)` and takes the invertible constant mixtures `T₁,T₁+T₂,T₁+T₃,T₁+T₄` of its coordinate partials. These are again coordinate partials in a linearly changed ambient coordinate system, but all four top symbols equal `2as²∂c`. Their common intrinsic LND `2a∂c` has image contained in `(a)` and plinth ideal `(a)`, so it does not even have an intrinsic slice. The suite checks the mixed coordinate inverse and all four top symbols exactly. Therefore neither generic-rank preservation nor an intrinsic-slice guarantee follows from the ambient coordinate origin.

No universal rank-repair theorem was obtained. To finish this global route one still needs an additional argument guaranteeing three independent commuting intrinsic LNDs, or another sufficiently strong structure on `K`. The facts that the ambient derivations commute, are coordinate partials, or are locally nilpotent do not justify the coefficient, commutator, or projection steps disproved here.
