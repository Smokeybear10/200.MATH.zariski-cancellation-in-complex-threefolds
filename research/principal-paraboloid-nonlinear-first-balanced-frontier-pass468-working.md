# The nonlinear first-potential branch is necessarily balanced

Working scoped synthesis: under EVERY actual hypothesis of264, assume
k=s+f, f_s=0 and n_ss*f''' nonzero. Then the strict degree alternative
is impossible, without needing an upper degree bound for its exclusion.
The remaining intrinsic degrees satisfy
\[
2\deg y=2\deg\theta=3\deg\sigma.
\tag{1}
\]
Combining with the earlier degree bound leaves the four necessary
pairs (deg sigma,deg y)=(2,3),(4,6),(6,9),(8,12). Their coefficient
functions are not classified and none is asserted to be realized.
In particular this is not recognition of the whole nonlinear branch.

## 1. Entire actual hypotheses

Retain the complete original-ring chart
[264](principal-one-affine-paraboloid-chart-pass264-working.md), its
genuine potential/minor input296 and arbitrary-n formulas458.
In particular
\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=A[u],\quad E=\partial_u,
\quad\deg_E(X,Y,Z,W)=(1,2,2,2),\\
I_{\rm initial}=(\mathsf X^2\mathsf Z-\mathsf Y^2)
\text{ is the ENTIRE weighted initial kernel},\\
X=a_0u+x_0,\quad a_0\in L^*,\quad x_0\in A,
\quad N=[u^4]\partial_Z|_A\ne0,\\
L=\operatorname{Frac}\ker_A N,\quad [L:\mathbb C(t,s)]<\infty,
\quad Nv=1,\\
O=L[A]=L[v]=L[y,\sigma,\theta]=L[y,z_{\rm int},w_{\rm int}],\\
\operatorname{Frac}A=L(v)=\mathbb C(y,z_{\rm int},w_{\rm int}),
\quad J_{t,s,v}(X)=-a_0^4\in L^*.
\end{gathered}
\tag{2}
\]
All other selected-partial, global-slice and localization conditions
remain required. The original slice is not normalized to X/a0.
Coefficient partials commute and have joint constants C. Put
\[
\mathbb F=\ker_L\partial_s,\qquad
[\mathbb F:\mathbb C(t)]<\infty,\qquad
k=s+f,\quad f\in\mathbb F,\quad e=n_{ss}\ne0,\quad f'''\ne0.
\tag{3}
\]
Primes on f mean exact t-derivatives. No rationality of the coefficient
fields or sufficiency of formal equations for actual entry is assumed.

## 2. Exact degree split and its two boundary exclusions

The complete
[462](principal-paraboloid-constant-sigma-nonlinear-first-slope-exclusion-pass462-working.md)
excludes constant sigma, including zero, even without f''' nonzero.
The separate
[463](principal-paraboloid-affine-sigma-irrational-residue-exclusion-pass463-working.md)
excludes degree one using the original scalar and the finite-field
norm obstruction. Thus a=deg(sigma)>=2.

The full centered cubic and tangent-minor proof
[460](principal-paraboloid-nonlinear-first-slope-tangent-degree-reduction-pass460-working.md)
gives
\[
\begin{gathered}
n=\frac e2s^2+\nu_0s+n_0,\quad e,\nu_0,n_0\in\mathbb F,
\quad e_s=0,\\
\deg x=\deg q=\deg y=\deg\theta=r,\qquad 2r\ge3a.
\end{gathered}
\tag{4}
\]
Here x,q are the exact affine centerings of460; their corrections
have degree at most a, strictly below r. There are only two logical
alternatives: equality in (4), or strict inequality.

## 3. The entire strict alternative is impossible

Assume 2r>3a. The exact degree-ratio proof
[461](principal-paraboloid-strict-nonlinear-degree-ratio-pass461-working.md)
gives r=2a. With P=sigma, its shear z=x-eta*q has degree a and
the whole return is O=L[P,z,q]. Its full third and fourth levels
and primitive tangent component remain required.

Since a>1, the refinement
[465](principal-paraboloid-strict-degree-parity-refinement-pass465-working.md)
applies. It writes a=2c, c>=1, and gives exact remainders
\[
z=\lambda P+S,\quad \deg S=c,\qquad
q=-P^2+R,\quad \deg R=3c,
\quad \lambda=\frac{f'''}{12\eta}\ne0.
\tag{5}
\]
The relation zW, with W the genuine tangent component, has exact
degree 4c-1. Its complete coefficient expansion is retained in465.
The degree argument includes zero lower coefficients and keeps the
half-degree tie; it does not by itself exclude that tie.

The independent residual descent
[467](principal-paraboloid-strict-residual-descent-pass467-working.md)
handles it. In its notation U=S^2+delta*P has degree at most c,
and V=U-mu*S has degree less than c, allowing either residual to
be zero. The exact transformed zW is
\[
\frac{12\eta^2\lambda}{\delta^2}S^4V+
\widetilde{\mathcal R}_4(S,V),\qquad
\deg_{S,V}\widetilde{\mathcal R}_4\le4,
\quad\delta\ne0.
\tag{6}
\]
Any positive degree of V gives a unique term of degree greater
than4c, contradicting deg(zW)=4c-1. Thus V is constant and P,z
belong to L[S]. The third level gives q in L(S); the elementary
intersection L(S) intersect L[v]=L[S] then puts q in L[S] as well.
Whole generation forces L[S]=L[v], so c=1 and a=2. This proof
works for every positive c, not just a finite degree list.

Finally the independently proved parity exclusion
[466](principal-paraboloid-strict-quadratic-sigma-parity-exclusion-pass466-working.md)
rules out exactly this a=2,r=4 case. After a temporary scalar
extension and affine intrinsic change, P=v^2+p0. The full odd
fourth relation and even part of W force a polynomial whose
quadratic coefficient first makes C=0 and whose linear coefficient
is then 8eta^2, nonzero. Its divisibility proof uses a dimension-two
quotient, so repeated roots are included. It does not assume that
a similar parity involution exists at higher intrinsic degrees.

This contradiction exhausts the strict alternative. The constant
and affine boundaries were already excluded separately in Section2.
No upper degree bound is used in this strict exclusion.

## 4. Remaining balanced conditions and finite frontier

Only 2r=3a remains. The balanced part of460 proves
\[
\begin{gathered}
f''''\ne0,\qquad
\eta=\frac{\operatorname{lc}x}{\operatorname{lc}q}
     =-\frac{4ef'''}{f''''}\in\mathbb F^*,
\qquad\eta^2+e/2\ne0,\\
4f'''f''''e_t=e(f'''')^2-32e^2(f''')^2.
\end{gathered}
\tag{7}
\]
Every denominator in (7) is known nonzero. These equations are
necessary, not sufficient for the original scalar, minor unit or
an actual chart.

The reviewed
[synthesis464](principal-paraboloid-nonlinear-first-potential-finite-frontier-pass464-working.md)
applies only the elementary Sections1--4 of299 to the genuine cubic
and quartic. It proves r<=12 from the gcd, homogenization and
whole-line growth argument. Combining this with a>=2 and 2r=3a
gives precisely
\[
\boxed{(a,r)\in\{(2,3),(4,6),(6,9),(8,12)\}.}
\tag{8}
\]
The stronger strict exclusion has removed every strict entry of464.
The four remaining entries are degree patterns, not four numerical
cases or four proven examples.

## 5. Evidence and scope

Root read the complete current465 in f93918,466 in ebaa0f and467 in
4c292a. Fresh7cb4a8 reconstructed the full zW coefficient ledger;
fresh257716 reconstructed its final residual substitution and every
monomial of (6). Freshd15503 independently checked the entire parity
identity used by466. All residuals were zero. Separate complete
component-source reviews and this synthesis's held-source review
belong in the research ledger.

All earlier264/296/458 and recognition dependencies remain retained;
no recursive certification of the full historical project is claimed.
This theorem does not recover an invariant coordinate or recognize
the balanced branch. It does not establish constant coupling, force
an arbitrary cancellation candidate into the supplied chart, or
resolve other initial kernels and time-degree profiles.

The full cancellation conjecture is unsolved. No saved checker was
executed, imported, compiled or rerun. No historical novelty, human
expert review, Lean certification, publication or outreach is claimed.
