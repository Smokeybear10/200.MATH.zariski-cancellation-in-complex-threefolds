# Filtered invariant-coordinate lifting

This note investigates one possible route to complex three-dimensional affine-space cancellation: start with a locally nilpotent derivation `D` on `B=C[x1,x2,x3,x4]` having a slice, find an invariant coordinate for its leading derivation, and lift it to an invariant coordinate of `D`. The route has two distinct steps. Under strictly positive weights the coordinate step is elementary. The invariant step can fail, even for a derivation that is already conjugate to a translation.

The complete proofs below give a finite sufficient test and explicit obstructions. They do not establish the missing universal lifting statement or a new result in the literature. The Vénéreau and stable-coordinate route is investigated separately.

## Positive weights make coordinate lifting elementary

Let `w1,...,wn` be strictly positive integers. For a nonzero polynomial `f`, write `deg_w(f)` for its largest monomial weight and `in_w(f)` for the sum of terms with that weight. This note uses highest, not lowest, weight initial forms.

**Proposition 1.** If `in_w(f)` is a polynomial coordinate of `k[x1,...,xn]`, then `f` is a polynomial coordinate. More precisely, one of the displayed variables occurs in `f` with a nonzero constant coefficient and has no other occurrence in `f`.

**Proof.** Put `p=in_w(f)` and `m=deg_w(f)>0`. Because `p` is a coordinate, it is the first component of a polynomial automorphism. The derivative matrix of that automorphism at the origin is invertible, as follows by differentiating its polynomial inverse. In particular `dp(0)` is nonzero. Thus some variable `xi` has a nonzero linear coefficient `c` in `p`.

Weighted homogeneity forces `wi=m`. Strict positivity means every monomial containing `xi`, other than `xi` itself, has weight greater than `m`. No such monomial can occur in `f`. Therefore

\[
f=cx_i+g(x_1,\ldots,\widehat{x_i},\ldots,x_n),\qquad c\ne0.
\]

Replacing `xi` by `f` has polynomial inverse `xi=(f-g)/c`. ∎

This proof does not require the Jacobian conjecture or a theorem asserting that a constant Jacobian implies invertibility. The actual inverse is displayed.

There is an immediate consequence for invariant lifting. If a polynomial invariant `q` has a coordinate as its positive-weight initial form, then `q` is an ambient coordinate. In dimension four, a slice derivation has regular kernel, and an invariant ambient coordinate puts it under Bhatwadekar, Gupta, and Lokhande, Theorem 3.5.[^1] That theorem then makes its kernel a three-variable polynomial ring.

The unsettled part is obtaining the invariant `q` with the prescribed initial form.

## An exact finite test for one proposed lift

Fix `D`, the positive integer weights, and a weighted homogeneous coordinate `p` of weight `m`. Let

\[
F_{m-1}B=\operatorname{span}_k\{x^\alpha:w\cdot\alpha<m\}.
\]

This vector space is finite dimensional. Form the matrix `M` whose columns are the polynomials `D(x^alpha)` for its monomial basis, expressed in a common monomial basis of a finite-dimensional target space containing those columns and `D(p)`. Let `b` be the coefficient column of `-D(p)`.

**Proposition 2.** If `rank(M)=rank([M|b])`, solving `Mc=b` produces an invariant ambient coordinate

\[
q=p+\sum_{w\cdot\alpha<m}c_\alpha x^\alpha.
\]

**Proof.** The linear equation is exactly `D(q)=0`. Its lower-weight terms do not change `in_w(q)=p`. Proposition 1 supplies a polynomial coordinate inverse. ∎

No local nilpotence is required for this finite test itself. For the cancellation application, the supplied derivation must separately be proved locally nilpotent and have a slice. The preceding theorem then finishes the implication for every successful certificate.

Failure is also an exact result: no invariant with this particular initial form exists. It does not rule out a different initial form, different weights, nonlinear changes of ambient coordinates, or a polynomial kernel. No uniform weight or degree bound covering all slice derivations is supplied here. Introducing a search parameter without proving such a bound does not turn this into a decision procedure for the conjecture.

This criterion is the invariant-lifting equation in computable form. Its value is that the polynomial-coordinate conclusion needs no further search once the finite linear equation is solved. It should not be advertised as a new universal lifting theorem.

## Invariants of the leading derivation need not lift

For a filtered derivation with leading derivation `delta`, one has an inclusion

\[
\operatorname{gr}(\ker D)\subseteq\ker\delta.
\]

This is the inclusion recorded in the standard filtered formalism; it is not an equality assertion.[^2] The following slice example makes the failure explicit.

On `B=k[x,y,z,w]` in characteristic zero, set

\[
D=\partial_x+x\partial_y,\qquad D(z)=D(w)=0.
\]

It is locally nilpotent, as successive derivatives terminate on all generators. It has slice `x`. With standard total degree its leading derivation is

\[
\delta=x\partial_y.
\]

Thus `x` is an invariant ambient coordinate of `delta`. But an element of initial form `x` must be `x+c`, and `D(x+c)=1`. There is no invariant lift with this initial form.

The kernel can be computed completely:

\[
\ker D=k[y-x^2/2,z,w].
\]

Indeed, `(x,y-x^2/2,z,w)` is a polynomial coordinate system, and `D` is differentiation in its first coordinate. For standard total degree, the initial forms of nonzero polynomials in these kernel generators give

\[
\operatorname{gr}(\ker D)=k[x^2,z,w]
\quad\subsetneq\quad
\ker\delta=k[x,z,w].
\]

To justify the displayed graded kernel exactly, the leading monomials of `(y-x^2/2)^a z^b w^c` are nonzero scalar multiples of `x^(2a) z^b w^c`. Distinct triples give distinct monomials, so leading terms cannot cancel to produce an odd power of `x`.

The example proves more than loss of a slice after taking leading terms: a specific invariant coordinate in the limiting action does not lift at all, even though cancellation already holds for the original action.

### The first obstruction in a deformation

Introduce a parameter `h` and define

\[
\mathcal D_h=h\partial_x+x\partial_y,
\qquad \mathcal D_h(h)=\mathcal D_h(z)=\mathcal D_h(w)=0.
\]

This is the homogenized family connecting `D` and `delta`. Suppose an invariant lift of `x` existed even modulo `h²`:

\[
Q=x+h a_1(x,y,z,w)\pmod{h^2}.
\]

Then

\[
\mathcal D_h(Q)
=h\bigl(1+x\partial_y a_1\bigr)\pmod{h^2}.
\]

The required equation is `x ∂y(a1)=-1`, which is impossible in the polynomial ring because its left side is divisible by `x`. This is an obstruction at the first correction, before questions about convergence or infinitely many corrections arise. Localizing at `x` would remove this particular divisibility obstruction but would change the global problem.

## A solved translation that every such positive-weight search misses

The finite test above can miss an invariant coordinate for every system of positive weights in the displayed coordinates. It can even miss after every linear coordinate change. A two-variable example proves the limitation without relying on an unresolved case.

Define

\[
a=x+y^2,\qquad b=y+a^2.
\]

These are polynomial coordinates, with inverse

\[
y=b-a^2,\qquad x=a-(b-a^2)^2.
\]

The derivation which is `∂/∂a` in these coordinates is

\[
D=(1+4ay)\partial_x-2a\partial_y.
\]

Direct differentiation gives `D(a)=1` and `D(b)=0`, so `D` is locally nilpotent and `ker D=k[b]`. Both compositions of the displayed coordinate formulas are identities by substitution.

For a constant direction `v=(alpha,beta)`,

\[
\partial_v b=\beta+2a(\alpha+2\beta y).
\]

For nonzero `v`, this is never a nonzero constant. If it were constant, the polynomial product `a(alpha+2 beta y)` would be constant; since `a` is nonconstant, this forces `alpha=beta=0`.

Every nonconstant invariant is `P(b)`. If `∂v P(b)` were a nonzero constant, the identity

\[
\partial_v P(b)=P'(b)\partial_v b
\]

would express a nonzero constant as a product in `k[x,y]`. Both factors would be nonzero constants, contradicting the previous calculation. Thus no nonconstant invariant has a nonzero constant directional derivative.

By Proposition 1, any invariant with coordinate initial form under positive weights would have a nonzero constant partial derivative in one of the displayed variables. After a linear coordinate change, that partial derivative would be a nonzero constant directional derivative in `(x,y)`. Both possibilities are excluded.

Consequently positive-weight initial-coordinate certificates are incomplete even for this explicit translation. A nonlinear ambient coordinate change reveals `b` immediately. This two-variable example is a limitation of the method, not a four-variable cancellation counterexample. Adjoining two fixed variables would make those new variables trivial invariant coordinates, so that extension would not establish the same all-weights failure in four variables.

## Mixed weights and formal completion introduce a different failure

Strict positivity in Proposition 1 matters. In `k[t,x,z,w]`, give `x` weight `1`, `t` weight `-2`, and give `z,w` any positive weights. For

\[
q=x+t x^2
\]

the highest-weight part is the coordinate `x`: its two terms have weights `1` and `0`. But `q=x(1+tx)` is not a coordinate. Both factors are nonunits and remain nonzero in the quotient by their product, so that quotient has zero divisors. Quotienting by a polynomial coordinate would give a polynomial domain.

The polynomial even has no critical points: if `∂t(q)=x²` vanishes, then `x=0`, where `∂x(q)=1+2tx` equals `1`. It therefore also shows why smoothness of a polynomial map does not force it to be a coordinate. It cannot be a slice of a locally nilpotent derivation in characteristic zero, since the slice theorem would identify its quotient with the domain given by that derivation's kernel. Its role here is to refute unrestricted mixed-weight and formal coordinate lifting, not the slice cancellation statement.

At the same time, the substitution `x↦x+t x²` has an inverse in the `t`-adic completion:

\[
x=u-tu^2+2t^2u^3-5t^3u^4+14t^4u^5-\cdots
 =\sum_{n\ge0}(-1)^n C_n t^n u^{n+1},
\]

where `C_n` are the Catalan numbers. The series is characterized by `x+t x²=u`; coefficient comparison gives the recurrence `C_0=1`, `C_n=Σ_{i+j=n-1} C_i C_j`, which verifies the identity at every order. The solution congruent to `u` modulo `t` is unique by successive coefficient comparison, so both compositions are identities in the completion.

The relevant completed ring is `k[x,z,w][[t]]`, the inverse limit of `k[t,x,z,w]/(t^N)`. It permits unbounded degrees in `x` as the order in `t` increases. It is larger than `k[[t]][x,z,w]`, whose elements have finite degree in the polynomial variables. The inverse above does not lie in the latter ring. If it did, passing to `k((t))[x]` would give a polynomial inverse to a univariate polynomial of degree two, contrary to multiplication of degrees under composition.

Thus compatible coordinate inverses to every finite order can exist while the global polynomial inverse does not. A proof via formal completion needs a separate argument for polynomial termination or algebraization. Smoothness at a point does not supply that argument.

## What a successful filtered argument would have to add

The first required addition is a theorem ensuring that at least one useful coordinate of `ker delta` belongs to `gr(ker D)`, or directly constructing an invariant that passes the finite criterion. The inclusion of graded kernels does not provide this theorem. The deformation example shows that the first obstruction need not vanish just because `D` has a slice.

The second requirement depends on the filtration. With strictly positive weights, Proposition 1 finishes coordinate lifting once the invariant lift exists, but the solved two-variable example shows that arbitrary positive weights and linear changes of variables may still miss all useful invariant coordinates. If a nonlinear change of coordinates is inserted, its existence must be proved rather than assumed.

With mixed weights, localization, or completion, even lifting a coordinate polynomial is a separate problem. The factorization example shows the danger explicitly. Clearing denominators, checking omitted fibers, and proving polynomial inverse formulas are mathematical obligations that remain after local or formal calculations succeed.

These results make the missing step more precise. They do not rule out a more effective filtration or a condition special to four-variable slice derivations. They do rule out several unrestricted lifting assertions that would otherwise appear to finish the conjecture.

## Sources

[^1]: S. M. Bhatwadekar, Neena Gupta, and Swapnil A. Lokhande, *Some K-theoretic properties of the kernel of a locally nilpotent derivation on k[X1,...,X4]*, January 7, 2015, Theorem 3.5. [Primary-source full text](https://arxiv.org/html/1501.01438v1). Used only for the implication from a nonzero locally nilpotent derivation fixing an ambient coordinate, with regular kernel, to a polynomial kernel. The theorem is not re-proved in this note.

[^2]: Bachar Alhajjar, *The Filtration Induced by a Locally Nilpotent Derivation*, October 14, 2013, Section 1.2, Definition 1.5 and the observation immediately following it; Section 2, Proposition 2.2. [Primary-source full text](https://arxiv.org/html/1310.3784v1). Used for the established filtered-derivation formalism and the inclusion of graded kernels. All particular counterexamples, finite tests, and elementary proofs in this note are supplied explicitly and are not attributed as new theorems of that paper.

## Addendum: a complete slice classification for one nonlinear extension family

The following argument resolves the slice question for an explicit infinite family of four-variable locally nilpotent derivations. It arose from testing a prospective cancellation candidate. The result excludes the nonconstant members as candidates, because they have no slice. No claim that the family or the argument is new in the literature is made.

Let `k` be a field of characteristic zero and put

\[
f=xz-y^2,\qquad
g=zf^2+2x^2yf+x^5,\qquad
r=-x^3-fy.
\]

On `k[x,y,z]` define the Jacobian derivation

\[
\Delta(H)=\det\frac{\partial(f,g,H)}{\partial(x,y,z)}.
\]

Its values can be written compactly as

\[
\Delta x=2fr,\quad
\Delta y=5x^5+4x^2yf-zf^2,\quad
\Delta z=2xf^2-10xyr.
\]

Direct polynomial identities give

\[
\Delta f=\Delta g=0,\qquad
r^2+f^3=xg,\qquad
\Delta r=fg.
\]

For any `a(x)∈k[x]`, extend this derivation to

\[
D_a=\Delta+a(x)\partial_w
\quad\text{on}\quad k[x,y,z,w].
\]

**Theorem.** The derivation `D_a` has a polynomial slice if and only if `a` is a nonzero constant. It is fixed-point-free if and only if `a(0)≠0`.

### Local nilpotence

First, every displayed `D_a` really is locally nilpotent. In the fraction field, with `f` and `g` inverted, the identities yield

\[
x=\frac{r^2+f^3}{g},\qquad
y=\frac{-r-x^3}{f},\qquad
z=\frac{g+2x^2r+x^5}{f^2}.
\]

Thus `x,y,z` are polynomials in `r` of degrees at most `2,6,10`, with coefficients fixed by `Delta`. Since `Delta r=fg` is fixed, repeated differentiation terminates on all three generators. In particular `Delta³x=Delta⁷y=Delta¹¹z=0`. The same is true of `a(x)`, so repeated differentiation of `w`, whose first derivative is `a(x)`, also terminates. The repeated Leibniz rule extends termination from the generators to every polynomial.

The fraction-field calculation is used only to prove polynomial identities about iterated derivatives. It does not assert that a rational coordinate change is a global polynomial automorphism.

### Fixed points

The zeros of `Delta` are exactly the line `x=y=0`. To prove this over an algebraic closure, suppose all three displayed derivative values vanish. If `f=0`, the formula for `Delta y` gives `x=0`, and `f=xz-y²=0` then gives `y=0`. If `f≠0`, the formula for `Delta x` gives `r=0`, then the formula for `Delta z` gives `x=0`, and `r=-x³-fy` gives `y=0`, contradicting `f≠0`. Conversely all the derivatives vanish when `x=y=0`.

Along this line `D_a(w)=a(0)`. This proves the fixed-point assertion. In particular, if `a(0)=0`, a slice is impossible because `D_a(s)` vanishes at the origin for every polynomial `s`.

### The orbit obstruction when `a(0)≠0`

Suppose now that `a` is nonconstant and `a(0)≠0`. Write `a(X)=Σ a_jX^j` and define the polynomial

\[
I(H)=\int_0^1a\bigl(H(u^2-u)\bigr)\,du
=\sum_j a_j(-1)^j\frac{(j!)^2}{(2j+1)!}H^j.
\]

The integral here is entirely algebraic: on polynomials it is the linear functional `u^n↦1/(n+1)`. The coefficient formula follows from integrating `u^j(1-u)^j`, or from its finite binomial expansion. All displayed scalar coefficients are nonzero in characteristic zero. Consequently `deg I=deg a>0`, while `I(0)=a(0)≠0`.

Over an algebraic closure `L` of `k`, choose a root `h≠0` of `I` and put `q=4/h`. Introduce an indeterminate `e`, and consider the polynomial family of points

\[
P_e=(0,e,qe^2,0).
\]

At this point the invariants and the auxiliary polynomial are

\[
f=-e^2,\qquad g=qe^6,\qquad r=e^3.
\]

Let `Phi_t` be the polynomial flow of `D_a`. Because `f` and `g` are fixed, the first and auxiliary coordinates along this orbit are

\[
r(t)=e^3-qe^8t,\qquad
x(t)=-2e^5t+qe^{10}t^2.
\]

Set

\[
T=\frac{2}{qe^5}\in L(e).
\]

Then `x(T)=0` and `r(T)=-e³`. Since `f=-e²` and `g=qe⁶` remain fixed, the definitions give `y(T)=-e` and `z(T)=qe²`. For the remaining coordinate, substitute `t=uT` to obtain

\[
x(uT)=\frac4q(u^2-u)=h(u^2-u),
\]

and hence

\[
w(T)-w(0)=\int_0^T a(x(t))\,dt
=T I(h)=0.
\]

We have proved the exact identity over `L(e)`

\[
\Phi_T(P_e)=Q_e:=(0,-e,qe^2,0).
\]

If `s∈k[x,y,z,w]` were a slice, it would remain a slice after extending scalars to `L`. The finite exponential identity for `D_a(s)=1` would give

\[
s(Q_e)-s(P_e)=T=\frac{2}{qe^5}.
\]

The left side belongs to `L[e]`, because both endpoint families have polynomial coordinates. The right side has a pole at `e=0`. The equality is impossible in `L(e)`. Thus no polynomial slice exists, in any degree. This contradiction is purely algebraic and does not require an analytic limit or a theorem about proper group actions.

Finally, if `a=c∈k*`, then `w/c` is a slice. Together with the fixed-point case, this proves the classification over every characteristic-zero field. Passing to an algebraic closure in the obstruction is legitimate because any slice defined over the original field would survive that scalar extension.

### A short certificate for `a(x)=1+lambda x`

For `lambda≠0`, the polynomial above is `I(H)=1-lambda H/6`. Thus one can take

\[
h=6/\lambda,\qquad q=2\lambda/3,\qquad
T=3/(\lambda e^5).
\]

The explicit orbit identity becomes

\[
\Phi_{3/(\lambda e^5)}
\left(0,e,\frac{2\lambda e^2}{3},0\right)
=
\left(0,-e,\frac{2\lambda e^2}{3},0\right).
\]

Both endpoint families extend polynomially across `e=0`; their required translation time has a pole. This is a compact certificate against a slice. The action is nevertheless fixed-point-free. For `lambda=0`, `w` itself is a slice.

### Comparison with the coefficient `1+f`

The related extension `Delta+(1+f)∂w` has a different short no-slice proof. Quotient by the invariant equation `f=-1`. The three-variable quotient can be expressed as

\[
R=k[x,r,g]/(xg-r^2+1),
\]

with descended derivation `delta x=-2r`, `delta r=-g`, `delta g=0`. The extended derivation now fixes `w`, so a purported slice would descend further under `w=0` to a slice for `delta` on `R`.

After inverting `g`, this ring is `k[g,g^-1,r]` and the kernel is `k[g,g^-1]`. Intersecting with `R` gives exactly `k[g]`: a Laurent polynomial with a genuine negative power of `g` cannot belong to `R`, as multiplying by the smallest necessary power and reducing modulo `g` would give a nonzero constant equal to zero. If `delta` had a slice `s`, the slice theorem would give `R=k[g][s]`. Its quotient by `g` would then be a polynomial domain, whereas actually

\[
R/(g)=k[x,r]/(r^2-1)
\]

has zero divisors. This contradiction verifies the alternative obstruction in all degrees as well.

### Extension to every coefficient in `k[x,f]`

The classification remains true for the larger family

\[
D_a=\Delta+a(x,f)\partial_w,\qquad a\in k[X,F]:
\]

there is a polynomial slice exactly when `a` is a nonzero constant. The fixed-point criterion becomes `a(0,0)≠0`. Local nilpotence follows by the same generator argument because `f` is fixed.

If `a(0,0)=0`, the fixed-point argument applies. Suppose `a(0,0)≠0` and `deg_X(a)>0`. Write `a(X,F)=Σ a_j(F)X^j` and, over `k((e))`, define

\[
I_e(H)=\sum_j a_j(-e^2)(-1)^j\frac{(j!)^2}{(2j+1)!}H^j.
\]

The substitution `k[F]→k[[e]]`, `F↦-e²`, is injective, so `I_e` is nonconstant. Its coefficients lie in `k[[e]]`, and its constant coefficient is a unit. Choose a root `h` in a finite algebraic extension `L` of `k((e))`. Its constant term is nonzero, so `h≠0`.

Choose a valuation ring `V` of `L` dominating `k[[e]]`; existence is the valuation-ring domination lemma.[^3] Let `m_V` denote its maximal ideal. If `h∈m_V`, all positive-degree terms of `I_e(h)` would lie in `m_V`, while its constant term would be a unit. Thus `h∉m_V`. The defining divisibility property of a valuation ring then gives `1/h∈V`: if `h∈V` it is a unit, and if `h∉V` its inverse belongs to `V`. Put `q=4/h∈V`.

The orbit calculation above still applies, with `f=-e²` and `a(x,f)` in place of `a(x)`. It gives

\[
\Phi_T(0,e,qe^2,0)=(0,-e,qe^2,0),\qquad
T=2/(qe^5),
\]

because the `w` displacement is `T I_e(h)=0`. Both endpoints have coordinates in `V`. But `e∈m_V` and `q∈V`, so `q e⁵∈m_V` and `T∉V`. A polynomial slice would make the difference of its two endpoint evaluations, which belongs to `V`, equal to `T`. This is impossible. No expansion of the algebraic root into a Puiseux series is needed.

It remains to handle coefficients `a(F)` independent of `X`. If such a polynomial is nonconstant and `a(0)≠0`, choose a root `c≠0` over an algebraic closure. Quotient by the invariant equation `f=c`; then `D_a(w)=a(c)=0`, so quotienting further by `w=0` would send any slice to a slice on

\[
R_c=k[x,r,g]/(xg-r^2-c^3),\qquad
\delta x=2cr,\quad\delta r=cg,\quad\delta g=0.
\]

The same localization-and-intersection argument gives `ker(delta)=k[g]`. A slice would imply `R_c=k[g]^[1]`, whereas `R_c/(g)=k[x,r]/(r²+c³)` has zero divisors over the algebraic closure because `c≠0` and the quadratic has two distinct roots. This completes the larger-family classification. The elementary univariate proof remains the shortest certificate for `a∈k[x]`.

[^3]: The Stacks Project, Section 10.50, Lemma 10.50.2, existence of a valuation ring of a field dominating a given local subring. [Primary-source statement and proof](https://stacks.math.columbia.edu/tag/00I8). Used only to choose `V` dominating `k[[e]]` in the finite extension `L`; the ensuing unit and pole argument is given explicitly above.

### Complete classification for invariant coefficients

A different extension family permits nonconstant coefficients and explicit slices. For

\[
D_a=\Delta+a(f,g)\partial_w,\qquad a\in k[F,G],
\]

the exact criterion is

\[
D_a\text{ has a polynomial slice}
\quad\Longleftrightarrow\quad
a(f,g)=c+fgP(f,g),\quad c\in k^*,\ P\in k[F,G].
\]

**Sufficiency.** Since `Delta(P)=0` and `Delta(r)=fg`,

\[
s=\frac{w-P(f,g)r}{c}
\]

is a slice. It is a polynomial coordinate because its coefficient of `w` is the nonzero constant `1/c`. Hence this entire successful subfamily has polynomial kernel. More explicitly, write `U=exp(-s Delta)(x,y,z)`, a finite polynomial expression. Here the exponential means the polynomial flow with an independent parameter, followed by substituting `-s`; it does not mean taking powers of the variable-coefficient derivation `-s Delta`. Then `(U,s)` is a coordinate system. The inverse starts with `(x,y,z)=exp(s Delta)U` and recovers `w=cs+P(f,g)r` from those coordinates. This verifies the kernel as `k[U1,U2,U3]`.

**Necessity.** If `a(0,0)=0`, the common fixed line excludes a slice. Assume `a(0,0)≠0` and extend the field to an algebraic closure if needed.

Suppose first that the restriction `a(F,0)` is nonconstant. Choose a root `c≠0`, so that `a(c,g)=g b(g)`. On the invariant quotient `f=c`, replace the fourth variable by

\[
w'=w-b(g)r/c.
\]

Its derivative is zero. Quotienting by `w'=0` would therefore send a slice to a slice for `Delta` on `R_c`. The preceding Danielewski-fiber argument shows that no such slice exists.

Suppose instead that `a(0,G)` is nonconstant. Choose a root `d≠0`, so that `a(f,d)=f b(f)`. On the invariant quotient `g=d`, the variable

\[
w'=w-b(f)r/d
\]

is fixed. A slice would descend under `w'=0` to one on

\[
S_d=k[x,y,z]/(g-d).
\]

Here are the domain and kernel details needed for that contradiction. The polynomial `f=xz-y²` is irreducible, and it does not divide `g-d` because modulo `f` the latter is `x⁵-d`. Unique factorization gives `(g-d):f=(g-d)`, so multiplication by `f` on `S_d` is injective. The explicit inverse formulas already displayed show

\[
(S_d)_f=k[f,f^{-1},r],\qquad
\Delta=fd\partial_r.
\]

Thus `S_d` embeds in a domain and is itself a domain. The kernel after localization is `k[f,f^-1]`. Its intersection with `S_d` is `k[f]`: a genuine negative power of `f` would, after clearing the smallest denominator and reducing modulo `f`, equate a nonzero scalar with zero. The quotient `S_d/(f)` is nonzero and equals

\[
k[x,y,z]/(xz-y^2,x^5-d)
\cong \bigl(k[x]/(x^5-d)\bigr)[y].
\]

The isomorphism uses the invertibility of `x`, since `x⁵=d≠0`, to set `z=y²/x`. Over the algebraic closure, this quotient is a product of five polynomial rings in one variable. If `Delta` had a slice on `S_d`, its kernel calculation and the slice theorem would give `S_d=k[f]^[1]`, whose quotient by `f` would be a domain. This is a contradiction.

Both axis restrictions must therefore be constant. Their constants agree with `a(0,0)=c≠0`. The polynomial `a(F,G)-c` vanishes on both axes, so it is divisible by `FG`. This proves necessity and completes the criterion.

### The plinth ideal underlying the invariant-coefficient criterion

The preceding calculations also identify

\[
\ker\Delta=k[f,g],\qquad
\ker\Delta\cap\Delta(k[x,y,z])=fg\,k[f,g].
\]

For the first equality, localization at `fg` gives `k[f,f^-1,g,g^-1,r]`, whose kernel is `k[f,f^-1,g,g^-1]`. To see that its intersection with the original polynomial ring has no genuine negative powers of `f`, reduce a denominator-cleared relation modulo `f`: the substitution `g=x⁵` makes `k[g]→k[x,y,z]/(f)` injective. To exclude genuine negative powers of `g`, evaluate the denominator-cleared relation on the line `x=z=0`, where `g=0` and `f=-y²`; this makes `k[f]` injective. Thus every invariant belongs to `k[f,g]`. Algebraic independence of `f,g` is also direct: evaluating at `x=0` gives `f=-y²`, `g=zy⁴`, so a polynomial relation in `f,g` would have all coefficients zero when expanded in `z`.

Write the second intersection as the plinth ideal `J`, an ideal of the kernel because multiplying a derivative by an invariant is still a derivative. The identity `Delta(r)=fg` gives `fg k[f,g]⊂J`.

Conversely, let `p(f,g)∈J`. On every fiber `f=c≠0`, the induced plinth ideal is an ideal of `k[g]` containing `g`, by `Delta(r)=cg`. It cannot contain `1`, by the proved no-slice obstruction, so it is exactly `(g)`. Hence `p(c,0)=0` for every nonzero `c`, giving `p(F,0)=0`. The same argument on every fiber `g=d≠0`, whose kernel is `k[f]` and whose plinth contains `f`, gives `p(0,G)=0`. Over the infinite characteristic-zero field, vanishing at all nonzero constants forces both polynomial identities. Therefore `FG` divides `p(F,G)`, proving `J=fg k[f,g]`.

For this particular derivation, the invariant-coefficient slice condition can consequently be expressed as `(a,J)=k[f,g]`. The explicit axis arguments prove necessity for slices of every polynomial degree; no assumption that a slice is linear in `w` was made.

### A further concrete coefficient: `a=1+y`

The extension `D=Delta+(1+y)∂w` is fixed-point-free, but the same orbit construction excludes a slice in every degree. Along the orbit starting at `(0,e,qe²,0)`, with `T=2/(qe⁵)`, the identity `y=-(r+x³)/f` gives

\[
y(uT)=e(1-2u)+\frac{64}{q^3e^2}(u^2-u)^3.
\]

Since the algebraic integral of `(u²-u)³` from zero to one is `-1/140`,

\[
\int_0^1 y(uT)\,du=-\frac{16}{35q^3e^2}.
\]

After adjoining a constant `C` with `C³=16/35`, put `e=H³` and `q=C H^-2` for a new indeterminate `H`. The integral of `1+y(uT)` is zero, and the exact orbit identity is

\[
\Phi_{(2/C)H^{-13}}(0,H^3,CH^4,0)
=(0,-H^3,CH^4,0).
\]

A slice would make its polynomial difference between these two endpoint families equal to `(2/C)H^-13`, which is impossible. The calculation settles this coefficient only; no classification for arbitrary polynomials involving `y` is asserted here.
