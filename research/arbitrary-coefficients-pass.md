# Arbitrary vertical coefficients: what the next pass establishes

This note concerns the extension question, not a proof or disproof of complex Zariski cancellation. Write `R=k[x,y,z]`, with characteristic-zero field `k`, and retain

\[
f=xz-y^2,\qquad g=zf^2+2x^2yf+x^5,\qquad
r=-x^3-fy,\qquad \Delta=\operatorname{Jac}(f,g,\cdot).
\]

The established identities are

\[
\Delta f=\Delta g=0,\quad \Delta r=fg,\quad
\Delta x=2fr,\quad r^2+f^3=xg.
\]

The classification for `a∈k[x,f,g]`, and the separate first-`f`-pole theorem, are proved in [extension-normal-forms.md](extension-normal-forms.md). They do not by themselves classify `\Delta+a\partial_w` for arbitrary `a∈R`.

## 1. The gauge implication fails for general base derivations

For a general LND `δ`, existence of a slice for `δ+a∂w` does **not** imply that `a=c+δH` with `c∈k*` and `H` polynomial.

Take `δ=x²∂y` on `k[x,y]`, and set

\[
E=x^2\partial_y+(1+xy)\partial_w.
\]

The polynomial

\[
s=w+\frac{y^3}{2}+\frac{xy^4}{8}
-xyw-\frac{x^2y^2w}{2}+\frac{x^3w^2}{2}
\]

satisfies `Es=1`. On the other hand, `δ(k[x,y])=x²k[x,y]`. If `1+xy=c+δH`, reduction modulo `x` forces `c=1`, whereas reduction modulo `x²` leaves the nonzero term `xy`. Thus there is no such polynomial primitive.

This is a counterexample to a proposed implication about extensions. It is not a cancellation counterexample. The explicit automorphism in the next section proves directly that this action has polynomial kernel. It also matters that the base derivation here is divisible by `x²`; this example does not decide the corresponding implication for the fixed irreducible rank-three derivation `Δ`.

## 2. A general automorphism certificate for replica constructions

The nonlinear slice above belongs to a broad class whose kernels can be identified constructively.

**Lemma.** Let `δ` be an LND on a `k`-domain `T`, where `k` is a characteristic-zero field. Let `b∈kerδ`, and suppose `F∈T` satisfies

\[
\delta F=ba,\qquad a\in T.
\]

On `T[w]`, set

\[
\widetilde\delta=\delta+a\partial_w,
\qquad h=F-bw,
\qquad E=b\delta+(1+\delta F)\partial_w.
\]

Then the polynomial automorphism

\[
\alpha=\exp(h\widetilde\delta)
\]

satisfies

\[
E=\alpha\partial_w\alpha^{-1},\qquad
\ker E=\alpha(T),\qquad E\alpha(w)=1.
\]

In particular, if `T` is a polynomial ring, so is `ker E`.

**Proof.** The extension `\widetildeδ` is locally nilpotent: its restriction to `T` is `δ`, and its successive derivatives of `w` are `a,δa,δ²a,...`, which eventually vanish. Also `\widetildeδh=δF-ba=0`, so `h\widetildeδ` is locally nilpotent. Its exponential is therefore a genuine polynomial automorphism with inverse `exp(-h\widetildeδ)`.

Using the bracket convention `[P,Q]=PQ-QP`,

\[
[h\widetilde\delta,\partial_w]=b\widetilde\delta,
\qquad
[h\widetilde\delta,b\widetilde\delta]=0.
\]

Consequently conjugation gives

\[
\alpha\partial_w\alpha^{-1}
=\partial_w+b\widetilde\delta
=b\delta+(1+ba)\partial_w=E.
\]

This proves all the assertions. No assumption that a local slice is an ambient coordinate is being made. ∎

### The quadratic local-slice construction

Suppose `δr=b∈kerδ` and take `F=r²/2`. Then `δF=br` and

\[
E=b\delta+(1+br)\partial_w,
\qquad h=\frac{r^2}{2}-bw.
\]

Here `\widetildeδ=δ+r∂w`, and the coordinate slice is

\[
\begin{aligned}
\alpha(w)
&=w+rh+\frac b2h^2\\
&=w+\frac{r^3}{2}+\frac{br^4}{8}
-brw-\frac{b^2r^2w}{2}+\frac{b^3w^2}{2}.
\end{aligned}
\]

For every base generator `z_i`,

\[
\alpha(z_i)=\left.\exp(t\delta)(z_i)\right|_{t=h}.
\]

The exponential is first taken with an independent indeterminate `t`, and then evaluated at `h`. Local nilpotence makes it a finite polynomial. The automorphism lemma, not substitution of a variable time alone, certifies invertibility.

For an additional direct inverse check, put

\[
v=r+bh,\quad s=\alpha(w),\quad h'=bs-v^2/2.
\]

Then `h'=-h`, and the inverse formulas are

\[
z_i=\left.\exp(t\delta)(\alpha(z_i))\right|_{t=h'},
\qquad
w=s+vh'+\frac b2(h')^2,
\]

where the first formula is interpreted in the new base coordinates. In particular the proposed action

\[
fg\Delta+(1+fg\,r)\partial_w
\]

has a fully explicit polynomial coordinate system and polynomial kernel. It is outside the original fixed-base family `Δ+a∂w`, and it cannot serve as an exotic-kernel candidate.

### Every polynomial in the local slice

More generally, take a polynomial `F(T)∈(kerδ)[T]` and evaluate it at `r`. Then

\[
E=b\delta+(1+bF'(r))\partial_w
\]

has the same certificate, with `h=F(r)-bw` and `\widetildeδ=δ+F'(r)∂w`. Its slice is the finite polynomial

\[
\alpha(w)=w+
\sum_{j\ge1}\frac{b^{j-1}h^j}{j!}F^{(j)}(r).
\]

When `b≠0` it can also be written

\[
\alpha(w)=w+\frac{F(r+bh)-F(r)}b,
\]

but the displayed finite Taylor sum is the polynomial meaning of this apparent quotient. Invariant coefficients in `F` cause no extra derivatives.

## 3. Affine-in-`w` slices for the fixed rank-three base

The following argument independently checks and simplifies the affine-slice reduction. By itself it does not reduce an arbitrary nonlinear slice to an affine one; the higher-pole proof later supplies that conclusion for this fixed base.

**Proposition.** Suppose `a∈R` and `E=Δ+a∂w` has a slice of the form

\[
s=u(f,g)w+v,\qquad u\in k[f,g],\ v\in R.
\]

Then `a=c+ΔH` for some `c∈k*` and `H∈R`. The converse is immediate, with slice `(w-H)/c`.

**Proof.** The slice equation is

\[
\Delta v+ua=1.
\]

The fixed locus of `Δ` is `x=y=0`, whose image under `(f,g)` is `(0,0)`. Restriction to this line shows that `u(0,0)≠0`. Extend scalars to an algebraic closure if needed.

We claim `u` has no zero on either coordinate axis of `Spec k[f,g]`. Suppose an irreducible factor `q` of `u` vanishes at `(0,d)`, `d≠0`, or at `(c,0)`, `c≠0`. Let `V` be the DVR at a normalization branch of the integral curve `q=0` over that point, and let `K` be its fraction field. Since `q` is neither `f` nor `g`, the generic values of both `f,g` are nonzero.

The map `(f,g):A³→A²` is smooth above `A²\{(0,0)}`: its Jacobian has rank two wherever `Δ` is nonzero, and all zeros of `Δ` map to the origin. This provides the needed flatness without appealing to a global theorem about LND quotient maps. Therefore `R_V=R⊗_{k[f,g]}V` is `V`-flat and embeds into its generic fiber

\[
(R_V)_K=K[r].
\]

The equation `u=0` in `V` gives `Δv=1` in `R_V`. The slice theorem yields `R_V=S[v]`, where `S=ker(Δ|_{R_V})`. The generic kernel is `K`, so

\[
V\subseteq S\subseteq K.
\]

An intermediate ring between a DVR and its fraction field is either the DVR or the field: any element with negative valuation makes a uniformizer invertible. The special fiber of `R_V` is nonempty, so `S≠K`; hence `S=V` and `R_V=V[v]`.

This is impossible at the selected point. At `(f,g)=(c,0)` with `c≠0`, the actual fiber has two disjoint affine-line components, from `r²=-c³`. At `(0,d)` with `d≠0`, it has five disjoint affine-line components, from `x⁵=d`. The fiber of `V[v]` is a single affine line. Thus neither axis contains a zero of `u`.

Over an algebraically closed field, each univariate restriction `u(f,0)` and `u(0,g)` must consequently be a nonzero constant. Their common value at the origin gives

\[
u=c_0+fgQ,\qquad c_0\in k^*.
\]

The same identity holds over the original field since it is a coefficient condition. Put `b=fg` and consider the `k[f,g]`-module `N=R/ΔR`. Every element of `N` is killed by some power of `b`: after inverting `b`, the ring is `k[f^{±1},g^{±1},r]` and `Δ=b∂r`, whose image is the whole localized ring. Also `b[1]=0` because `Δr=b`.

Multiplication by `u=c_0+bQ` is injective on `N`. Indeed, on an element killed by `b^m`, the finite geometric series in `-bQ/c_0` gives its inverse. The slice equation gives `u[a]=[1]`, and

\[
u\bigl([a]-c_0^{-1}[1]\bigr)
=[1]-c_0^{-1}(c_0+bQ)[1]=0.
\]

Injectivity implies `[a]=c_0^{-1}[1]`. Thus `a=c_0^{-1}+ΔH`, as claimed. ∎

For a purported affine slice written initially as `u(x,y,z)w+v`, the coefficient of `w` in `Es` forces `Δu=0`; hence the hypothesis `u∈k[f,g]` is automatic.

## 4. The full coefficient ring `C[r]` is also classified

Put `C=k[x,f,g]` and

\[
L(P)=gP+2(xg-f^3)P_x.
\]

The previously established classification extends to every coefficient in

\[
C[r]=C\oplus rC\subset R.
\]

For `a∈C[r]`, the extension `Δ+a∂w` has a slice if and only if `a=c+ΔH` for a nonzero constant `c` and a polynomial `H∈R`.

To see this, write `a=A+rB`, `A,B∈C`, decompose `A=A_0(x,f)+L(P)` using `C=L(C)⊕k[x,f]`, and choose `U∈C` with `U_x=B/2`. Then

\[
a=A_0(x,f)+\frac{\Delta(rP+U)}f.
\]

The symmetric-orbit argument in the next section proves that a slice forces `A_0=c∈k*`. In this case the first-pole theorem applies directly to the polynomial `rP+U∈R`: it has a removable invariant residue exactly when the extension has a slice, and then the coefficient differs from `c` by an actual polynomial derivative. This proves the assertion.

The odd and even parts can cancel each other's primitive obstruction. For example,

\[
3gx-2f^3+8x^3r=\Delta(-xy).
\]

Thus adding the odd term `8x³r` converts the known nonslice coefficient `1+3gx-2f³` into a coefficient with the explicit slice `w+xy`. Testing the two parts separately would miss this cancellation.

## 5. Every arbitrary-coefficient slice reduces to a higher `f` pole

**Theorem.** Let `a∈R` be arbitrary. If `E=Δ+a∂w` has a polynomial slice, then there are `c∈k*`, an integer `m≥0`, and a polynomial `H∈R` such that

\[
a=c+\frac{\Delta H}{f^m}.
\]

The conclusion alone is a necessary representation, not an assertion that the displayed pole can always be removed. The case `m=0` is already a polynomial primitive, and `m=1` is covered by the first-pole theorem. Section 8 supplies the higher-pole argument.

**Algebraic normal form.** After inverting `f`,

\[
R_f=C_f\oplus rC_f,
\qquad
C_f=L(C_f)\oplus k[x,f,f^{-1}].
\]

The second direct sum is the localization of the established `k[f]`-linear decomposition. Therefore write

\[
a=A+rB,
\quad A=A_0(x,f)+L(P),
\quad A,B,P\in C_f,
\quad A_0\in k[f,f^{-1}][x].
\]

Choose `U∈C_f` with `U_x=B/2`. Then

\[
a=A_0(x,f)+\frac{\Delta(rP+U)}f.
\tag{1}
\]

Clearing the finitely many `f` denominators in `rP+U` will produce the theorem once `A_0` is proved to be a nonzero constant.

**A rescaled symmetric orbit.** A slice forces

\[
a(0,0,z)=c\in k^*.
\]

Indeed, on the fixed line of `Δ`, the slice equation becomes `a(0,0,z)∂_ws(0,0,z,w)=1` in `k[z,w]`.

Use independent parameters `e,Q`, with endpoints

\[
p=(0,e,Q),\qquad q=(0,-e,Q).
\]

Their common invariants are `f=-e²`, `g=Qe⁴`, and their `Δ`-time difference is

\[
T=\frac{2}{Qe^3}.
\]

For an independent orbit parameter `u`, put `v=u²-u`. The triple at time `uT` is

\[
\begin{aligned}
x(uT)&=\frac{4e^2v}{Q},\\
y(uT)&=e(1-2u)+\frac{64e^4v^3}{Q^3},\\
z(uT)&=Q+\frac{32e^3(1-2u)v^2}{Q^2}
        +\frac{1024e^6v^5}{Q^5}.
\end{aligned}
\tag{2}
\]

These formulas follow from `r(uT)=e³(1-2u)` and the identities expressing `x,y,z` through `f,g,r`. All coefficients lie in `k[e,Q,Q^{-1}]`, and the triple reduces to `(0,0,Q)` modulo `e`.

Define the polynomial integral

\[
J_a(e,Q)=\int_0^1 a(x(uT),y(uT),z(uT))\,du.
\]

Characteristic zero makes the integral a finite coefficientwise operation. Thus

\[
J_a\in k[e,Q,Q^{-1}],\qquad J_a\equiv c\pmod e.
\tag{3}
\]

If `J_a` had a nonzero negative power of `Q`, let `-d<0` be the smallest exponent and put `F(Q)=Q^dJ_a(e,Q)`. This is a polynomial over `k[[e]]`, its constant coefficient is nonzero, and its coefficient of `Q^d` is a unit by (3). In a finite splitting extension of `k((e))`, at least one root `Q_0` has nonnegative valuation. Otherwise every reciprocal root would have positive valuation; the factorization

\[
F(Q)=F(0)\prod_i(1-Q/\rho_i)
\]

would make every nonconstant coefficient have positive valuation, contrary to the unit coefficient of `Q^d`. Since `F(0)≠0`, the selected root is nonzero.

At `Q=Q_0`, the full `E`-flow joins `(p,0)` to `(q,0)`: its fourth-coordinate displacement is `T J_a(e,Q_0)=0`. Both endpoints are integral in the valuation ring, whereas `T=2/(Q_0e³)` has negative valuation. A polynomial slice would give their slice-value difference equal to `T`, a contradiction. Consequently a slice forces `J_a` to have no negative powers of `Q`.

**Reading the normal form from its moments.** Write `A_0=Σ_j a_j(f)x^j`. Since `r` changes sign under `u↦1-u` while `x,f,g` remain fixed, the average of `rB` is zero, including when coefficients have `f` denominators. Also

\[
\int_0^1 L(P)\,du=gP(0,f,g),
\]

because `Δ(rP)=fL(P)` and the endpoint values of `r` are `e³,-e³`. Therefore

\[
J_a(e,Q)=
\sum_{j\ge0}\gamma_j a_j(-e^2)e^{2j}Q^{-j}
+Qe^4P(0,-e^2,Qe^4),
\quad
\gamma_j=\frac{4^j(-1)^j(j!)^2}{(2j+1)!}.
\tag{4}
\]

The last term contains only strictly positive powers of `Q`, even though its coefficients may initially be displayed with `e` denominators. The coefficient of `Q^{-j}`, `j>0`, is exactly the indicated nonzero scalar times `a_j(-e²)e^{2j}`. Hence the absence of negative powers forces every `a_j` for `j>0` to vanish. We conclude `A_0=a_0(f)`.

The constant coefficient in `Q` in (4) is `a_0(-e²)`. By (3) it belongs to `k[e]` and has constant `c`. A Laurent polynomial in `f` with this property has no negative `f` powers. Thus `a_0∈k[f]` and `a_0(0)=c`.

If `a_0` were nonconstant, choose a nonzero root `α` after extending the field. In the quotient `f=α`, the rational primitive `(rP+U)/f` from (1) is polynomial, because every denominator is a power of `f`. Shearing `w` by this primitive turns the descended action into `Δ`, with a fixed fourth coordinate. Quotienting by that coordinate would give a slice for `Δ` on `R/(f-α)`. This is impossible: its kernel is `k[g]`, but the fiber `g=0` is the union of two disjoint affine lines, whereas a slice would make the ring `k[g][s]`. Thus `a_0=c`, completing the proof. ∎

The passage from (4) to (3) is important. Separate terms of a normal form in `R_f` may have apparent `e` denominators. Integrality is justified by the original polynomial coefficient evaluated on the integral Laurent-polynomial orbit (2), not by assuming each unsimplified normal-form term is integral.

## 6. A genuine second-pole test, also excluded in all degrees

Consider

\[
S=x^2y+fz=\frac{rx^2+g}{f},\qquad a=1+S.
\]

This coefficient lies outside `C[r]`: its normal form has a genuine `f` denominator. Set

\[
H=r+x^3/6=-5x^3/6-fy.
\]

Then

\[
\Delta H=fg+fx^2r=f^2S.
\]

Thus `a=1+ΔH/f²`. There is no polynomial primitive of `S`, since `S` has total degree three while the homogeneous derivation `Δ` increases total degree by four. This observation alone does not exclude a nonlinear slice.

The rescaled symmetric average is `J_a=1-Qe²`, so that particular orbit test does not exclude a slice: its root `Q=e^{-2}` makes the endpoints nonintegral. A different degeneration resolves the example.

Let `ζ` be a primitive fifth root of unity, put `S_j(t)=1+t+...+t^j`, and introduce a small parameter `b`. There is a formal solution `t(b)` with `t(0)=ζ` to

\[
tS_4(t)+\frac{125}{216}b^9S_5(t)^3=0.
\tag{5}
\]

Indeed, `tS_4(t)` has a simple zero at `ζ`: `S_4=(t^5-1)/(t-1)` and `ζ≠1`. Thus formal coefficient comparison recursively determines the solution.

Set

\[
G=b^5S_5(t),\qquad F=-5G/6.
\]

Equation (5) is precisely `F³=b⁶tS_4(t)`. The two triples

\[
p=(b,0,F/b),\qquad q=(bt,0,F/(bt))
\]

therefore have common invariants `f=F`, `g=G`, with `r(p)=-b³` and `r(q)=-b³t³`. Their time difference is

\[
T=\frac{b^3(1-t^3)}{FG}.
\]

Since `S_5(ζ)=1`, both `F,G` have valuation five, while `1-t³` is a unit. Thus `T` has valuation `-7`. Both triples are integral: their first coordinates have valuation one, and their third coordinates have valuation four.

At these points `H=-5x³/6`, so

\[
H(q)-H(p)=\frac56b^3(1-t^3).
\]

The fourth-coordinate displacement for `Δ+(1+S)∂w` is consequently

\[
T+\frac{H(q)-H(p)}{F^2}
=\frac{b^3(1-t^3)}{F^2G}\left(F+\frac56G\right)=0.
\]

The full action joins two integral points with fourth coordinate zero at a time of negative valuation. No polynomial slice can exist. This proof covers every potential slice degree, but only the specified second-pole coefficient. It does not prove a general higher-pole removal theorem.

## 7. The complete second-pole argument

Suppose `c∈k*`, `f²|ΔH`, and `E=Δ+(c+ΔH/f²)∂w`. If the residue `h(x)=H modf` lies in `k[x⁵]`, subtract a matching invariant polynomial `P(g)` and divide the numerator by `f`; the established first-pole theorem decides the resulting action.

If `h∉k[x⁵]`, first subtract the invariant polynomial matching all terms of `h` whose exponents are divisible by five. We can then write

\[
H=h(x)+fK,
\]

where the smallest exponent `d` of `h` is positive and not divisible by five, with coefficient `h_d≠0`.

Set `F=b^{d+2}V` and solve for `t,V` as formal series in `b`, using

\[
\begin{aligned}
tS_4(t)&=b^{3d}V^3,\\
cV(1-t^3)+S_5(t)b^{-d}
\left[H(bt,0,F/(bt))-H(b,0,F/b)\right]&=0.
\end{aligned}
\]

The divided bracket is regular near `b=0,t=ζ`: the `h` part starts in degree `d`, and the `fK` part is divisible by `b^{d+2}`. At `b=0`, the second equation becomes

\[
cV(1-\zeta^3)+h_d(\zeta^d-1)=0.
\]

Its root `V_0` is nonzero. The Jacobian in the variables `t,V` is invertible: the first equation has nonzero `t` derivative and zero `V` derivative at `b=0`, and the second has nonzero `V` derivative `c(1-ζ³)`. Hence recursive formal lifting gives the desired series.

The two triples `(b,0,F/b)` and `(bt,0,F/(bt))` share invariants `f=F,g=b⁵S_5(t)`. The second equation says exactly that their fourth-coordinate displacement for `E` is zero. Their coordinates are integral, while their orbit time has valuation `3-(d+2)-5=-d-4`. This contradicts a polynomial slice.

Thus the second-pole action has a slice exactly when its rational primitive can be replaced by a polynomial primitive after adding an invariant rational function. In particular it has a slice exactly when `a-c∈ΔR`.

## 8. Higher poles: the complete working proof for the fixed base

The following argument supplies the higher-pole step. Its scope is the one fixed rank-three derivation `Δ`. Two independent model audits found no gap in the completed argument; these were not human expert review or peer review, and they do not establish novelty. The proof remains a working research result suitable for further external mathematical checking. No novelty claim is made.

**Higher-pole lemma.** Suppose `c∈k*`, `m≥1`, `H∈R`, and `f^m|ΔH`. If

\[
E=\Delta+\left(c+\frac{\Delta H}{f^m}\right)\partial_w
\]

has a polynomial slice, then `ΔH/f^m∈ΔR`.

For `m=1`, this is the proved first-pole theorem. If `H modf∈k[x⁵]`, subtract the matching invariant `P(g)` and divide the numerator by `f`, reducing `m` by one. It therefore remains to exclude a slice when `m≥2` and the residue `H modf=h(x)` is not in `k[x⁵]`. For this obstruction argument replace `k` by its algebraic closure. A slice over the original field would remain a slice after that extension, so proving nonexistence over the closure suffices.

### 8.1. Remove low homogeneous invariant terms

The derivation `Δ` is homogeneous of total degree four. Write `H=Σ_D H_D` in homogeneous components. For `D<2m-4`, divisibility of `ΔH` by `f^m` forces `ΔH_D=0` by degree. At `D=2m-4`, it would give

\[
\Delta H_D=\lambda f^m,\qquad\lambda\in k.
\]

The already proved polynomial-primitive criterion on `C` excludes a primitive of `f^m`. Equivalently, the plinth ideal is `fgk[f,g]`, which contains no nonzero scalar multiple of `f^m`. Thus `λ=0` as well.

Subtract these invariant components. They do not change `ΔH` and change `h(x)` only by terms in `k[x⁵]`. We may assume that every monomial of `H` has total degree

\[
D>2m-4.
\tag{6}
\]

The residue is still not in `k[x⁵]`.

### 8.2. Use exact branches with fixed `g`

Choose a primitive fifth root `ζ` after extending the field. Let `φ(Z)∈k[[Z]]` be the unique series satisfying

\[
\phi(Z)^6-\phi(Z)+Z=0,\qquad\phi(0)=1.
\]

It exists because the derivative at `1` is `5`. For independent symbols `B,F`, write `Z=F³/B⁶` and define

\[
X_0=B\phi(Z),\qquad
X_1=\zeta B\phi(\zeta^{-1}Z).
\tag{7}
\]

Both satisfy `X_i^6-B⁵X_i+F³=0`. Consequently the triples

\[
p_i=(X_i,0,F/X_i)
\]

have common invariants `f=F,g=B⁵`. Also `r_i=-X_i³`.

These exact branches prevent a subtle error. Raw monomials with exponent divisible by five do not necessarily disappear from the endpoint difference when the branch parameter is only approximately `ζ`. Their higher-order corrections must be included. Formula (7) includes them explicitly.

### 8.3. Expand the endpoint difference and preserve the degree bound

Only `H(x,0,z)` contributes to these endpoints. For one of its monomials `a_{ij}x^iz^j`, put `l=i-j`. Since `x^iz^j=F^jx^l` at a point with `y=0`, expand

\[
\phi(Z)^l=\sum_{n\ge0}q_{l,n}Z^n.
\]

Negative integers `l` cause no problem because `φ` is a unit. The contribution to `H(p_1)-H(p_0)` is

\[
\sum_{n\ge0}
a_{ij}q_{l,n}
\left(\zeta^{l-n}-1\right)
B^{l-6n}F^{j+3n}.
\]

Put `L=l-6n` and `J=j+3n`. Because `ζ⁵=1`, the root-of-unity factor equals `ζ^L-1`. Most importantly,

\[
L+2J=i+j=D>2m-4.
\tag{8}
\]

Thus after collecting terms we have an expansion

\[
H(p_1)-H(p_0)=\sum_{J,L}d_{J,L}B^LF^J,
\tag{9}
\]

where every nonzero coefficient satisfies (8). For each fixed `J` there are only finitely many terms. Among terms with `0≤J<m-1`, there are finitely many in total, and at least one is nonzero: the `J=0` terms contain exactly `h(ζB)-h(B)`, which is nonzero by the residue hypothesis.

For these low-`J` terms, (8) implies

\[
L\ge2m-3-2J\ge1,
\qquad
\frac{L+2}{m-1-J}>2.
\]

Choose the rational number

\[
q=\min_{d_{J,L}\ne0,\;J<m-1}
\frac{L+2}{m-1-J}=\frac MN>2,
\tag{10}
\]

with positive integers `M,N`, and substitute

\[
B=t^N,\qquad F=t^M V.
\]

Because `M-2N>0`, all the series in (7) and (9) now converge `t`-adically, with polynomial coefficients in `V`. The third coordinates `F/X_i` have valuation `M-N>0` whenever `V` is a unit.

### 8.4. The leading equation always has a nonzero root

The fourth-coordinate displacement vanishes precisely when

\[
\mathcal E(t,V):=
H(p_1)-H(p_0)
+cF^{m-1}\frac{r_1-r_0}{B^5}=0.
\tag{11}
\]

Let `k_0=(m-1)M-2N`. The second term in (11) has leading term

\[
c(1-\zeta^3)t^{k_0}V^{m-1}.
\]

Every term in (9) has valuation at least `k_0`. For `J<m-1`, this follows from the minimality in (10). For `J≥m-1`, use (8) to compute the strict inequality

\[
NL+MJ-k_0
=N\bigl(D-2m+4\bigr)
 +(J-m+1)(M-2N)>0.
\tag{12}
\]

Therefore `t^{-k_0}\mathcal E(t,V)` belongs to `k[V][[t]]`. Its reduction modulo `t` is the polynomial

\[
P(V)=c(1-\zeta^3)V^{m-1}
+\sum_{NL+MJ=k_0}d_{J,L}V^J.
\tag{13}
\]

The sum contains at least one nonzero term, all with `J<m-1`. There is no cancellation between different terms of the same power `V^J`: on the chosen line `NL+MJ=k_0`, a given `J` determines `L` uniquely, and coefficients were already collected in (9).

Factoring out the smallest occurring power of `V` from (13) leaves a positive-degree polynomial with nonzero constant term. Over an algebraic closure it has a root `V_0≠0`.

The root need not be simple. Put `Y=V-V_0` and apply formal Weierstrass preparation to `t^{-k_0}\mathcal E(t,V_0+Y)` in `k[[t,Y]]`. Its reduction at `t=0` is a nonzero polynomial having a finite positive-order zero at `Y=0`. Hence the series is a unit times a monic distinguished polynomial in `Y` over `k[[t]]`. A root of that polynomial in a finite valued extension of `k((t))` has positive valuation, so `V=V_0+Y` is a unit and (11) holds exactly. This is the usual complete-local preparation theorem, for example [Laurent Berger, Corollary 1.2](https://perso.ens-lyon.fr/laurent.berger/articles/article33.pdf). Multiple roots therefore do not invalidate the construction.

### 8.5. The orbit time has a pole

With the lifted unit `V`, all coordinates of `p_0,p_1` are integral. They lie on the same `Δ` orbit, with time

\[
T=\frac{r_1-r_0}{FB^5}.
\]

Since `r_1-r_0` has leading term `(1-ζ³)t^{3N}`, its valuation is exactly `3N`; hence

\[
\operatorname{val}(T)=3N-M-5N=-M-2N<0.
\]

Equation (11) says precisely that the fourth-coordinate displacement `cT+(H(p_1)-H(p_0))/F^m` is zero. Thus the `E`-flow joins `(p_0,0)` to `(p_1,0)` at a nonintegral time. A polynomial slice would make that time the difference of two integral polynomial values, a contradiction.

This excludes every minimal nonremovable pole with `m≥2`. Together with the first-pole theorem and the repeated invariant-subtraction reduction, it proves the higher-pole lemma. ∎

### Consequence for all vertical coefficients

Combining Section 5 with the higher-pole lemma gives the complete working classification for this fixed base:

\[
\boxed{
\Delta+a\partial_w\text{ has a polynomial slice}
\iff a=c+\Delta H\text{ for }c\in k^*,\ H\in R,
\qquad a\in R.
}
\]

In the positive case `(w-H)/c` is a slice and the ordinary polynomial shear followed by the finite `Δ` flow gives polynomial coordinates for the kernel. This statement is about all vertical extensions of one particular LND on `A³`; it does not classify arbitrary slice LNDs on `A⁴` and does not settle Zariski cancellation.

### Properness is equivalent as well, for this same fixed family

For `E=Δ+a∂w`, `a∈R`, let `Φ` denote its additive-group action. Call the action proper when its action morphism

\[
\mu:\mathbb G_a\times\mathbb A^4\longrightarrow
\mathbb A^4\times\mathbb A^4,
\qquad (T,p)\longmapsto(p,\Phi_T(p))
\]

is proper. The working classification above strengthens to

\[
\boxed{
\Phi\text{ is proper}
\iff E\text{ has a polynomial slice}
\iff a=c+\Delta H\quad(c\in k^*,\ H\in R).
}
\]

Here properness is algebraic properness of `μ`, not a claim that the quotient variety or affine space is proper over `k`.

**Proof.** First observe the precise valuative meaning of the endpoint obstruction. Suppose `V` is a valuation ring with fraction field `K`, `p,q∈A⁴(V)`, and `T∈K\V` satisfy `Φ_T(p)=q` over `K`. They give a `V`-point `(p,q)` of the target of `μ` and a compatible `K`-point `(T,p)` of its source. If `μ` were proper, the [valuative criterion for properness](https://stacks.math.columbia.edu/tag/0BX5) would extend this source point over `V`. Its first coordinate would extend `T` to an element of `V`, which is impossible. Thus every such integral-endpoint, pole-time certificate proves nonproperness directly, without assuming or discussing a slice.

A proper action cannot have a fixed point: the fiber of `μ` over the pair consisting of that point twice would contain the whole stabilizer `G_a`, and in fact equal it, whereas `G_a` is not proper. After extending to an algebraic closure, this forces `a(0,0,z)` to be a nonzero constant, exactly the fixed-line condition used in Section 5. A nonconstant polynomial on that line has a zero, and the identically zero polynomial also gives fixed points.

The rescaled-moment obstruction in Section 5 and the first- and higher-pole obstructions all construct the valuative certificate just described. The only excluded case originally handled by a slice-specific argument was the nonconstant one-variable remainder `a_0(f)`. That case also has an explicit nonproperness certificate.

Choose a nonzero root `α` of `a_0`. On the closed invariant fiber `f=α`, the `f`-localized primitive in (1) becomes polynomial. After shearing the fourth coordinate by it, the action is `Δ` on `R/(f-α)` with the fourth coordinate fixed. Choose `v≠0` with `v²=-α` and let `G` be a formal parameter. The two triples

\[
p=(0,v,G/\alpha^2),\qquad
q=(0,-v,G/\alpha^2)
\]

have `f=α`, `g=G`, and `r(p)=-αv`, `r(q)=αv`. Their exact `Δ`-time difference is

\[
T=\frac{r(q)-r(p)}{\alpha G}=\frac{2v}{G}.
\]

The triples are integral over `k[[G]]`, but this time has a pole. With fourth coordinate zero they give the required nonproperness certificate on the sheared fiber. Properness survives base change to a closed invariant subvariety: the restricted action morphism is the pullback of `μ` along that subvariety's product with itself. It also survives polynomial conjugacy. Therefore the original action cannot be proper in this last negative case either.

We have proved that a proper action survives all the same reductions and must have `a=c+ΔH`. Conversely, such an action is polynomially conjugate to translation on `A³×A¹`. The translation action morphism is a closed immersion onto the locus where the two `A³` coordinates agree, with inverse time given by the difference of the two `A¹` coordinates. A closed immersion is proper. This proves the equivalences. ∎

The special-fiber invariant identities and the time `2v/G` were also checked by exact Laurent-polynomial arithmetic. The corollary does not generalize properness-versus-translation to arbitrary additive-group actions on `A⁴`; it concerns only the fixed-base vertical family classified here.

### Genuine third- and fourth-pole examples

The standalone checker below also verifies the following exact identities, reconstructed with the Jacobian derivation rather than by differentiating the formal branches:

\[
\begin{aligned}
H_3&=x^6+\frac{12}{5}fx^3y+\frac{42}{25}f^2y^2,\\
\Delta H_3&=f^3 A_3,\\
A_3&=-\frac{12}{25}
\left(5x^3z+2x^2y^2+7xyz^2-7y^3z\right),
\end{aligned}
\]

and

\[
\begin{aligned}
H_4&=x^9+\frac{18}{5}fx^6y+\frac{117}{25}f^2x^3y^2
+f^3\left(\frac{312}{125}y^3+\frac95x^3\right),\\
\Delta H_4&=f^4 A_4,\\
A_4&=-\frac{72}{125}
\left(25x^5+35x^3yz-22x^2y^3+13xy^2z^2-13y^4z\right).
\end{aligned}
\]

Their residues are respectively `x⁶` and `x⁹`, so their primitive poles are nonremovable. Their exact collected Newton-edge slopes are `4` and `11/3`; the edge coefficients are respectively `ζ-1` and `ζ⁴-1`. The higher-pole lemma therefore excludes polynomial slices for both `Δ+(1+A_3)∂w` and `Δ+(1+A_4)∂w` in every degree. The finite checker verifies the identities and edges, while that last all-degree conclusion uses the written lemma.

## 9. Exact checks and scope of the conclusion

SymPy 1.13.3 was used with independent formal variables `b,r,w` and the derivation `E=b²∂r+(1+br)∂w`. Direct expansion verified

\[
Eh=-b,\quad Ev=0,\quad Es=1,\quad h'+h=0,
\quad s+vh'+b(h')^2/2-w=0.
\]

The substitution `b=x,r=y` independently verified the nongauge example in Section 1. The general polynomial formula was additionally checked for `F=r`, `r²/2`, `r³+r`, and `r⁵+br²+1`. These finite checks supplement the general automorphism proof; they are not the reason it holds for every polynomial `F`.

For a genuinely nonlinear candidate slice

\[
s=\sum_{i=0}^n v_iw^i,\qquad n>1,
\]

the coefficient equations are

\[
\Delta v_n=0,\qquad
\Delta v_i+(i+1)a v_{i+1}=0\ (1\le i<n),\qquad
\Delta v_0+a v_1=1.
\]

They do not imply that `v_1` is invariant. Applying the affine proposition to the last equation without proving `Δv_1=0` would therefore be an error. Likewise, absence of a polynomial primitive does not generally exclude a nonlinear slice, as Section 1 proves.

The earlier coefficient-by-coefficient equations do not by themselves produce an affine replacement. Section 8 instead gives an all-degree orbit obstruction for every nonremovable primitive pole. Two independent model audits checked the collected branch expansion, the degree inequality, and the formal root-lifting step without finding a gap. This is a completed working proof for the full fixed-base vertical family, not human mathematical certification. The broader question of arbitrary slice LNDs on four-variable polynomial rings remains untouched by that reduction.

The new [verify_higher_poles.py](../verify_higher_poles.py) uses only Python's standard library and exact rational and fifth-cyclotomic arithmetic. Its nine test groups passed in approximately half a second. They check `φ⁶-φ+U` through degree eleven, positive and negative series powers, both exact branches and the root-of-unity factor, the two genuine higher-pole primitives above, their Newton edges, and a finite degree/weight grid. Negative controls reject a corrupted series coefficient and primitive identity.

One deliberate expansion stress test is `H=x¹⁰+x³¹` at formal pole order five. It is not claimed to satisfy `f⁵|ΔH`. Its collected slope is `6`, while discarding raw fifth-divisible exponents would incorrectly give `33/4`. A separate check shows that all branch contributions of the actual invariant `g²` cancel after collection. These checks specifically guard against the raw-monomial error discussed in Section 8.2. They do not test an infinite series, prove Weierstrass preparation, or replace the general proof.

The slice and localization tools used here are standard; a primary-source introduction is [Harm Derksen's lecture notes on locally nilpotent derivations](https://sites.lsa.umich.edu/hderksen/wp-content/uploads/sites/614/2018/09/LND1.pdf). The explicit extension arguments in this note are supplied in full rather than attributed to a literature theorem. No novelty claim is made.
