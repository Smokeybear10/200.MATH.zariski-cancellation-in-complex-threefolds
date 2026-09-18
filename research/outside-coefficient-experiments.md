# Outside-`C` coefficients for the Freudenburg extension

**Date:** 2026-09-12  
**Status:** exact orbit calculations and a working all-degree theorem for coefficients of ordinary total degree at most two. This note does **not** settle the unrestricted coefficient problem, does not falsify or prove the proposed general gauge criterion, and makes no novelty claim.

## 1. Main outcome

Let

\[
R=k[x,y,z],\qquad f=xz-y^2,
\]

\[
g=zf^2+2x^2yf+x^5,\qquad r=-x^3-fy,
\]

and let `Delta=Jac(f,g,-)` over a characteristic-zero field. For `a in R`, put

\[
D_a=\Delta+a\partial_w\quad\text{on }R[w].
\]

The two requested geometrically free extensions have no polynomial slice:

\[
D_{1+xy}\text{ has no slice},\qquad
D_{1+y^2}\text{ has no slice}.
\]

These are all-degree conclusions, not failures of a bounded ansatz. More generally:

**Degree-two working theorem.** If `a in k[x,y,z]` has ordinary total degree at most two, then

\[
D_a\text{ has a polynomial slice}
\quad\Longleftrightarrow\quad
a\in k^*.
\]

The positive direction is the slice `w/a`. The negative direction is proved below with fixed points, exact paired-orbit certificates, and one nonzero-invariant-fiber argument. The proof has not received external or proof-assistant review.

There are also useful all-degree subfamilies outside `C=k[x,f,g]`:

\[
a=c+P(y),\qquad a=c+P(xy),
\]

where `c in k*` and `P(0)=0`. If `P` is nonzero, neither extension has a polynomial slice. Thus the method is not intrinsically limited to quadratic coefficients.

## 2. The symmetric orbit and the universal pole test

The identities

\[
\Delta f=\Delta g=0,\qquad \Delta r=fg,
\]

and

\[
r^2+f^3=xg,\qquad
y=-\frac{r+x^3}{f},\qquad
z=\frac{g+2rx^2+x^5}{f^2}
\]

give an exact one-parameter orbit. Work temporarily in a valued extension and take nonzero parameters `epsilon,q`. Start at

\[
p_+=(0,\epsilon,q\epsilon^2)
\]

and use the time

\[
T=\frac{2}{q\epsilon^5}.
\]

Then the endpoint is

\[
p_-=(0,-\epsilon,q\epsilon^2).
\]

Indeed, along the orbit `f=-epsilon^2`, `g=q epsilon^6`, and `r` changes from `epsilon^3` to `-epsilon^3`. At normalized time `uT`, put

\[
v=u^2-u,\qquad \kappa=1-2u.
\]

The complete first-three-coordinate path is

\[
\begin{aligned}
x(u)&=\frac{4v}{q},\\
y(u)&=\epsilon\kappa+\frac{64v^3}{q^3\epsilon^2},\\
z(u)&=q\epsilon^2
 +\frac{32\kappa v^2}{q^2\epsilon}
 +\frac{1024v^5}{q^5\epsilon^4}.
\end{aligned}
\tag{1}
\]

For a coefficient `a`, define the algebraic orbit average

\[
\mathcal A_a(\epsilon,q)=\int_0^1a(x(u),y(u),z(u))\,du.
\tag{2}
\]

This is just termwise integration of a finite polynomial in `u`; no analytic integration is being used. The fourth-coordinate displacement of the `D_a`-flow at time `T` is exactly

\[
T\mathcal A_a(\epsilon,q).
\]

Consequently, suppose a valued field `K` with valuation ring `V` admits `epsilon,q` such that

* both `(p_+,0)` and `(p_-,0)` belong to `V^4`;
* `T` does not belong to `V`;
* \(\mathcal A_a(\epsilon,q)=0\).

Then `D_a` has no polynomial slice. If a slice `s` existed, the finite exponential identity

\[
\exp(TD_a)(s)=s+T
\]

would give

\[
s(p_-,0)-s(p_+,0)=T.
\]

The left side lies in `V`, while the right side does not.

This pole test excludes slices of every possible polynomial degree.

## 3. Exact moments

The beta integral

\[
I_n=\int_0^1(u^2-u)^n\,du
=\frac{(-1)^n(n!)^2}{(2n+1)!}
\tag{3}
\]

is nonzero in characteristic zero. Reflection `u -> 1-u` also gives

\[
\int_0^1\kappa v^n\,du=0.
\]

Substitution in (1) yields

\[
\begin{array}{c|l}
\phi&\displaystyle\int_0^1\phi(x(u),y(u),z(u))\,du\\
\hline
x&-\dfrac{2}{3q}\\[4pt]
y&-\dfrac{16}{35q^3\epsilon^2}\\[4pt]
x^2&\dfrac{8}{15q^2}\\[4pt]
xy&\dfrac{128}{315q^4\epsilon^2}\\[4pt]
y^2&\dfrac{\epsilon^2}{3}+\dfrac{1024}{3003q^6\epsilon^4}\\[4pt]
xz&-\dfrac{2\epsilon^2}{3}+\dfrac{1024}{3003q^6\epsilon^4}\\[4pt]
yz&-\dfrac{32}{105q^2}+\dfrac{32768}{109395q^8\epsilon^6}.
\end{array}
\tag{4}
\]

The standalone checker `verify_outside_coefficients.py` reconstructs (1), checks `f,g,r` pointwise, and verifies every rational moment in (4) using only exact `Fraction` arithmetic.

## 4. The two requested coefficients

For `a=1+xy`, equation (4) gives

\[
\mathcal A_{1+xy}=1+\frac{128}{315q^4\epsilon^2}.
\]

Over an algebraic closure choose `theta` with

\[
\theta^4=-\frac{128}{315},
\]

and work in `kbar((s))` with

\[
\epsilon=s^2,\qquad q=\theta s^{-1}.
\]

Then the average is zero, the endpoint coordinate `q epsilon^2=theta s^3` is integral, and

\[
T=\frac{2}{\theta s^9}
\]

has a pole. The pole test proves nonexistence of a slice.

For `a=1+y^2`, equation (4) gives

\[
\mathcal A_{1+y^2}
=1+\frac{\epsilon^2}{3}
 +\frac{1024}{3003q^6\epsilon^4}.
\]

Choose `theta^6=-1024/3003`, let `U(s)` be the unique unit with constant term one satisfying

\[
U(s)^6=(1+s^6/3)^{-1},
\]

and set

\[
\epsilon=s^3,\qquad q=\theta s^{-2}U(s).
\]

The average again vanishes exactly. The endpoint `z`-coordinate is

\[
q\epsilon^2=\theta s^4U(s),
\]

while

\[
T=\frac{2}{\theta U(s)s^{13}}
\]

has a pole. This proves the second all-degree exclusion.

Both coefficients restrict to `1` on the fixed line `x=y=0` of `Delta`; the two actions are therefore geometrically free. They are concrete examples where freeness does not produce a slice.

## 5. Proof of the degree-two working theorem

It is harmless to extend scalars to an algebraic closure: a slice over `k` would remain a slice. A general coefficient of total degree at most two restricts on the fixed line to

\[
c+az+bz^2.
\]

If this polynomial is nonconstant, it has a root and `D_a` has a fixed point. If it is zero, the fixed line remains fixed. Thus a possible slice requires the restriction to be a nonzero constant `c`.

Using `xz=f+y^2`, every remaining coefficient has a unique expression

\[
a=c+\alpha x+\beta y+\gamma x^2+\delta xy
 +\lambda f+\mu y^2+\nu yz,
\qquad c\ne0.
\tag{5}
\]

Equations (4) give

\[
\begin{aligned}
\mathcal A_a={}&c-\frac{2\alpha}{3q}
-\frac{16\beta}{35q^3\epsilon^2}
+\frac{8\gamma}{15q^2}
+\frac{128\delta}{315q^4\epsilon^2}
-\lambda\epsilon^2\\
&+\mu\left(\frac{\epsilon^2}{3}
+\frac{1024}{3003q^6\epsilon^4}\right)
+\nu\left(-\frac{32}{105q^2}
+\frac{32768}{109395q^8\epsilon^6}\right).
\end{aligned}
\tag{6}
\]

The following elementary lifting observation handles coefficient cancellations
in the applications below. If

\[
\Psi(s,Q)\in\bar k[[s]][Q,Q^{-1}]
\]

has no negative `s`-valuation and `Psi(0,Q)` has a nonzero root `theta`,
then, after a finite valued extension, there is a unit `Q(s)` reducing to
`theta` with `Psi(s,Q(s))=0`. In each use below, clearing the negative powers
of `Q` produces a polynomial whose leading coefficient is a unit. To justify
multiple roots as well as simple ones, factor its reduction into the power of
`(Q-theta)` and a coprime complementary factor, and apply Hensel
factorization. A root of the lifted monic factor is integral and reduces to
`theta`. This is the elementary local form of the Newton--Puiseux step used
below.

Now inspect the first nonzero coefficient in the following order.

### Case 1: `nu != 0`

Set

\[
\epsilon=s^4,\qquad q=s^{-3}Q.
\]

Equation (6) has no negative `s`-powers and reduces to

\[
c+\frac{32768\nu}{109395Q^8}.
\]

It has a nonzero root, which lifts to a unit `Q(s)` making the full average zero. The endpoint `q epsilon^2=s^5Q(s)` is integral and `T=2s^{-17}/Q(s)` has a pole.

### Case 2: `nu=0` and `(beta,mu) != (0,0)`

Set

\[
\epsilon=s^3,\qquad q=s^{-2}Q.
\]

The reduction is

\[
c-\frac{16\beta}{35Q^3}
+\frac{1024\mu}{3003Q^6}.
\]

As a nonconstant polynomial in `Q^{-3}` with nonzero constant `c`, it has a nonzero root. After lifting, `q epsilon^2=s^4Q(s)` is integral and `T=2s^{-13}/Q(s)` has a pole.

### Case 3: `nu=beta=mu=0` and `delta != 0`

Set

\[
\epsilon=s^2,\qquad q=s^{-1}Q.
\]

The reduction is

\[
c+\frac{128\delta}{315Q^4}.
\]

Again it has a nonzero root. The endpoints are integral and `T=2s^{-9}/Q(s)` has a pole.

These three cases exhaust all coefficients in (5) genuinely outside `C=k[x,f,g]`.

### Case 4: only `c,alpha,gamma,lambda` remain

If `(alpha,gamma) != (0,0)`, set `epsilon=s` and `q=Q`. The reduction of (6) is

\[
c-\frac{2\alpha}{3Q}+\frac{8\gamma}{15Q^2}.
\]

It is nonconstant in `Q^{-1}` and has a nonzero root. A lifted unit `Q(s)` gives integral endpoints and a time with valuation `-5`.

If `alpha=gamma=0` and `lambda != 0`, put

\[
\alpha_0=-c/\lambda\ne0.
\]

On the invariant fiber `f=alpha_0`, the coefficient `c+lambda f` vanishes. A hypothetical slice descends through the stable quotients `f-alpha_0=0` and `w=0` to a slice for `Delta` on

\[
S_{\alpha_0}
=\bar k[x,r,g]/(xg-r^2-\alpha_0^3).
\]

After inverting `g`, this derivation is `alpha_0 g partial_r`, so its unlocalized kernel is `kbar[g]`. The slice theorem would force `S_{alpha_0}=kbar[g][s]`. But

\[
S_{\alpha_0}/(g)
=\bar k[x,r]/(r^2+\alpha_0^3)
\simeq\bar k[x]\times\bar k[x],
\]

whereas `kbar[g][s]/(g)` is a domain. This is impossible.

Only the constant `a=c in k*` survives, and it has the displayed linear slice. This proves the working theorem.

## 6. Two all-degree outside-`C` families

The same degeneration proves more than the quadratic statement.

Let `P(T)=sum_{j>=1}p_jT^j` be nonzero. For `a=c+P(y)`, take

\[
\epsilon=s^3,\qquad q=s^{-2}Q.
\]

At `s=0`, equation (1) gives `y=64v^3/Q^3`, so

\[
\mathcal A_a(0,Q)
=c+\sum_{j\ge1}p_j64^j I_{3j}Q^{-3j}.
\]

This is a nonconstant polynomial in `Q^{-3}` with constant `c`; every `I_{3j}` is nonzero. It therefore has a nonzero root, which lifts as above. The endpoint valuation is four and the time valuation is minus thirteen.

For `a=c+P(xy)`, take

\[
\epsilon=s^2,\qquad q=s^{-1}Q.
\]

Now `xy=256v^4/Q^4+O(s^3)`, and

\[
\mathcal A_a(0,Q)
=c+\sum_{j\ge1}p_j256^j I_{4j}Q^{-4j}.
\]

This is again nonconstant with nonzero constant and has a liftable nonzero root. The endpoint valuation is three and the time valuation is minus nine. Both entire families are therefore excluded in every polynomial slice degree.

## 7. Attempt to falsify the gauge criterion

The natural unrestricted conjecture is

\[
D_a\text{ has a slice}
\quad?\Longrightarrow\quad
a=c+\Delta H,qquad c\in k^*,\ H\in R.
\tag{7}
\]

It is false for general locally nilpotent derivations, so it cannot be assumed merely from triangularity of the extension. No counterexample for this particular irreducible `Delta` was found in this pass.

Writing a prospective slice as

\[
s=\sum_{i=0}^n s_iw^i
\]

gives the exact recurrence

\[
\Delta s_n=0,
\qquad
\Delta s_j+(j+1)a s_{j+1}=0\ (1\le j<n),
\qquad
\Delta s_0+a s_1=1.
\tag{8}
\]

Thus nonlinear slices are a genuine possibility: the top coefficient is an invariant, but it need not be a unit. In particular, a linear-in-`w` slice `s=qw+h` is equivalent to

\[
q\in k[f,g],\qquad \Delta h+qa=1.
\tag{9}
\]

For nonconstant `q`, equation (9) asks for a slice of the induced derivation on the invariant hypersurface `q(f,g)=0`; it does not algebraically permit division by `q`. This is a precise route by which (7) could fail.

A bounded exact quotient search was made for `q=1+g`, `q=1+f+g`, and `q=1+f+g^2`. No `h` of ordinary total degree at most twelve satisfying `Delta h=1 mod q` was found. For the control `q=1+fg`, degree three succeeds via `h=-r`, but the resulting extension is the known gauge case. These finite null results are diagnostics only and do not prove (7), even for linear-in-`w` slices.

The next structural target is therefore not another blind degree increase. It is to classify which invariant curves `q(f,g)=0` make the induced `Delta` admit a slice, and then determine whether every such lift forces `(1-Delta h)/q` back into `k^*+Delta(R)`. A separate higher-`w` analysis can start from recurrence (8).

## 8. Reproducibility and claim limits

Run the exact moment checker with

```bash
cd "/Users/thomasou/Documents/ChatGPT/Long term/zariski-cancellation"
python3 verify_outside_coefficients.py
```

Expected result: three tests pass, checking the orbit invariants, all eight moments in (4), and the two requested averages. The checker does not formalize Hensel factor lifting, the valuation contradiction, or the universal quantifier over slices.

The following distinctions are essential:

* the moment identities are machine-checked exact arithmetic;
* the degree-two and two univariate-family exclusions are written all-degree proofs;
* the invariant-curve searches are bounded diagnostics;
* criterion (7) remains unresolved for arbitrary `a in R`;
* none of these results implies characteristic-zero cancellation or has established publication priority.
