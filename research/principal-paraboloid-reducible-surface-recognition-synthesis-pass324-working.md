# Recognition for every reducible surface in the supplied paraboloid chart

Working synthesis: in the actual nonzero-coupling principal chart264, a
reducible monic surface level forces an invariant coordinate of the original
polynomial four-ring and hence a polynomial three-variable kernel. The
formal-constant factor difference, every genuine projected conic, and two
of the three projected-line branches are impossible. The remaining line
branch is recognized by313, not declared impossible.

This is an exhaustive composition within the supplied chart. It neither
establishes entry into that chart nor treats its irreducible surface
levels. No previous source, checker, index, or ledger is changed.

## 1. The actual hypotheses retained throughout

Let
\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=A[u],\qquad E=\partial_u,
\qquad A=\ker E,\\
\deg_E(X,Y,Z,W)=(1,2,2,2),\qquad
a=EX,\quad b=E^2Y/2,\quad c_Z=E^2Z/2,\quad e=E^2W/2.
\end{gathered}
\tag{1}
\]
Assume the **full** weighted initial kernel is
\[
\ker\bigl(\mathbb C[\mathsf X,\mathsf Y,\mathsf Z,\mathsf W]
 \longrightarrow A[T]\bigr)
 =(\mathsf X^2\mathsf Z-\mathsf Y^2),
\quad
(\mathsf X,\mathsf Y,\mathsf Z,\mathsf W)
 \longmapsto(aT,bT^2,c_ZT^2,eT^2).
\tag{2}
\]
Membership of this one polynomial in a larger initial kernel is not enough.
All four leaders are nonzero. Put \(t=b/a^2\), \(s=e/a^2\).
They are algebraically independent, and \(c_Z/a^2=t^2\).

The literal original partial \(T_Z=\partial_Z\) has exact shift four.
Its selected leading derivation is
\[
0\ne N=[u^4]T_Z|_A\in\operatorname{LND}(A),\qquad
Na=Nt=Ns=0.
\]
With \(L=\operatorname{Frac}\ker_A N\), the retained local-slice chart is
\[
[L:\mathbb C(t,s)]<\infty,\qquad
A\otimes_{\ker_A N}L=L[v],\qquad Nv=1,\qquad
K:=\operatorname{Frac}A=L(v).
\tag{3}
\]
The unique coefficient partials on L extending \(\partial_t,\partial_s\)
commute, fix v, and have joint constants \(\mathbb C\). No rationality
of L is assumed.

The fixed-actual-X map and its first two potentials are
\[
\begin{aligned}
Y&=y+\sigma X+tX^2,\\
Z&=z+(2t\sigma+k)X+t^2X^2,\\
W&=w+\theta X+sX^2,\\
z&=2ty+\sigma^2+k_t\sigma+m\theta+n,\\
mw+(2\sigma+k_t)y+F(\sigma,\theta)&=\ell,
\qquad m=k_s\ne0,
\end{aligned}
\tag{4}
\]
where \(k,n,\ell\in L\), the intercepts and intrinsic generators lie in
\(L[v]\), and
\[
F(P,V)=\frac{k_{tt}}2P^2+k_{ts}PV+\frac{k_{ss}}2V^2+n_tP+n_sV.
\]
In addition to these polynomial identities, the actual frame supplies
\[
\det\frac{\partial(Y,Z,W)}{\partial(t,s,v)}=-a^4\in L^*,\qquad
K=\mathbb C(y,z,w),\qquad
L[y,z,w]=L[y,\sigma,\theta]=L[v]=:O.
\tag{5}
\]
The field equality and both polynomial-ring equalities are retained, not
replaced by an arbitrary parametrization satisfying the potentials.
These entry facts are proved in
[264](principal-one-affine-paraboloid-chart-pass264-working.md).

For independent formal U,P,V define
\[
\begin{aligned}
g&=\frac{\ell-(2P+k_t)U-F(P,V)}m,\\
H&=U^2+F_PU+F_Vg+H_3(k;P,V)+H_2(n;P,V)-\ell_tP-\ell_sV,\\
H_0&=H-h_0\in L[U,P,V],\qquad H(y,\sigma,\theta)=h_0\in L.
\end{aligned}
\tag{6}
\]
Here \(H_j(f;P,V)=\sum_{i=0}^j
f_{t^{j-i}s^i}P^{j-i}V^i/((j-i)!i!)\), with formal variables held
fixed in coefficient differentiation. Thus H0 is monic quadratic in U
and has total degree at most three. Assume it is reducible **over the
exact field L**.

The actual scalar determinant also gives the unit gradient ideal of H
in O and the unit two-by-two minor ideal of the evaluated gradients of
H and the fourth potential Q. These are the retained conclusions of
[290](principal-paraboloid-nonzero-coupling-projection-pass290-working.md)
and [296](principal-paraboloid-fourth-potential-gradient-minors-pass296-working.md).
They are not smoothness assumptions imposed on a formal parametrization.

## 2. Statement and exhaustive reduction

Under (1) through (6), there is an actual coordinate \(Q_0\) of
\(\mathcal B\) such that
\[
EQ_0=0,\qquad A=\mathbb C[Q_0]^{[2]}\cong\mathbb C^{[3]}.
\tag{7}
\]
More precisely, the retained chart cannot occur in any of the excluded
rows below. Its only surviving branch satisfies \(m_s=0\) and
\(\sigma_v=0\), and313 supplies (7) there. This does not assert that
every formal instance of the surviving branch is realizable.

To see that the split is exhaustive, monicity gives
\[
H_0=(U+\mathsf A)(U+\mathsf B),\qquad
\mathsf A,\mathsf B\in L[P,V],\quad
\deg\mathsf A,\deg\mathsf B\le2,\quad
\deg(\mathsf A\mathsf B)\le3.
\tag{8}
\]
Exactly one factor vanishes on the actual line. Relabel it \(U+\mathsf A\).
The unit gradient ideal makes the other evaluated factor a unit, so
\[
y=-\mathsf A(\sigma,\theta),\qquad
L[\sigma,\theta]=O,\qquad
(\mathsf B-\mathsf A)(\sigma,\theta)=\eta\in L^*.
\tag{9}
\]
Let G generate the projected kernel in \(L[P,V]\). It is irreducible.
The whole polynomial-line return yields
\(\deg G=\max(\deg_v\sigma,\deg_v\theta)\), with pure-power top
homogeneous part. If the formal factor difference is nonconstant, G
divides \(\mathsf B-\mathsf A-\eta\), hence \(1\le\deg G\le2\).
The formal-constant alternative is separately controlled in302 and308.
These exact-field conclusions, including the degree bounds, are proved in
[302](principal-paraboloid-reducible-surface-conic-reduction-pass302-working.md).

| Reducible-surface case | Actual endpoint |
| --- | --- |
| Formal factor difference constant | Excluded by308 |
| Nonconstant difference, \(\deg G=2\) | Excluded by323, using302/306/315 |
| Nonconstant difference, \(\deg G=1\), \(m_s\ne0\) | Excluded by314/317 |
| Nonconstant difference, \(\deg G=1\), \(m_s=0\), \(\sigma_v\ne0\) | Excluded by310/312 |
| Nonconstant difference, \(\deg G=1\), \(m_s=0\), \(\sigma_v=0\) | Recognized by313 |

If G is a line, \(\sigma,\theta\) are affine in v. At least one factor
coefficient in (8) is affine, because two genuine quadratic factors
would have product degree four. Equation (9) therefore makes y affine
as well, regardless of which factor is selected. This is precisely
[309](principal-paraboloid-reducible-line-affine-generators-pass309-working.md).
It is not an ambient-coordinate assertion.

## 3. The exclusion endpoints preserve the actual hypotheses

**Constant difference.** The discriminant identities of302 force
\(k=ms+\kappa t^2/2+bt+d\), with all displayed coefficients complex
and \(m\ne0\). Only then is the polynomial change
\(W_*=mW+\kappa Z/2+bY+dX^2\) used. Its inverse, rebuilt coefficient
partials, both lower potentials, and full formal surface-level transport
are retained. The resulting exact coefficient family has the
original-ring square obstruction of
[308](principal-paraboloid-constant-factor-difference-exclusion-pass308-working.md):
a rational square root is integral over the normal original polynomial
ring, but its square has odd degree one in an actual coordinate. This
excludes the branch, rather than merely bounding its projected degree.

**Genuine conic.** The selected-factor analysis of
[306](principal-paraboloid-selected-conic-factor-rigidity-pass306-working.md)
forces the affine surface factor to be selected, \(m_s=0\), and
\(m=d+c/T\), where \(T=t-\tau\), \(c\in\mathbb C^*\), and
\(d,\tau\in\mathbb C\). It treats both initial factor selections.
Moreover \(\sigma\) is affine, \(O=L[\sigma]\), and the literal
intercepts are polynomials in \(\sigma\). The coefficient presentation
needed here is supplied by
[315](principal-paraboloid-conic-polynomial-coefficient-return-pass315-working.md).

The short obstruction in
[323](principal-paraboloid-all-conic-polynomial-specialization-exclusion-pass323-working.md)
uses no generic-plane descent theorem. Since E fixes L and \(\sigma\),
\(\sigma=EY/a-2tX\) proves the exact equality
\(L[\mathcal B]=L[X,\sigma]\). Write the quadratic intercept leaders
as \(y_2,z_2\) and the cubic leader of w as \(w_3\). Then
\[
\begin{aligned}
y_2&=-\frac{dc}{(c+dT)^2},&
z_2&=2ty_2+1+\frac{2c}{c+dT}\ne0,\\
w_3&=\frac{2c}{(c+dT)^2}\ne0,&
z_2-2ty_2&=\frac{3c+dT}{c+dT}\ne0.
\end{aligned}
\tag{10}
\]
The quadratic terms cancel in \(z_2Y-y_2Z\). Its linear
\(\sigma\)-coefficient has a nonzero X-slope, so specialization at its
root \(X=x_0\in L\) makes that combination constant. The whole L-ring
equality survives specialization and would make polynomials of exact
degrees two and three generate \(L[\sigma]\). Quadratic centering and
the odd-module calculation in323 rule this out. The specialization holds
the coefficient field fixed; it is not differentiation at a moving root.

**Variable coupling line.** If \(m_s\ne0\), the actual normalization of
[314](principal-paraboloid-variable-coupling-hodograph-reduction-pass314-working.md)
puts \(k^2=2h(t)s\), with h a nonzero complex polynomial of degree at
most two. It includes full formal surface-level transport before a
selected curve is imposed. The full lower-factor integrations and literal
Jacobian calculation in
[317](principal-paraboloid-variable-coupling-line-exclusion-pass317-working.md)
exclude both projected-line directions and both factor selections.
The proof retains \(h'=0\); it does not divide by h' or assume a
preferred selected factor. The transformed calibrated determinant is
still a nonzero coefficient-field scalar, contradicted either by its
vanishing or by its nonzero X-coefficient.

**s-independent coupling, varying sigma.** In the line branch with
\(m_s=0\), \(\sigma_v\ne0\), and nonconstant formal factor difference,
[310](principal-paraboloid-line-legendre-field-reduction-pass310-working.md)
first proves the complex coefficients needed for its actual reframe.
It then obtains an exact finite normalization of the coefficient-extended
original ring. This is only a rational-entry and finite-ring reduction,
not polynomial entry by itself.

[312](principal-paraboloid-legendre-conductor-exclusion-pass312-working.md)
supplies the missing obstruction: for its explicit rings R and N, a free
rank-two presentation gives the conductor exactly \(DN\). The original
E extends as an explicitly triangular LND on N, so the conductor is
E-stable. Thus \(D\mid ED\), hence \(ED=0\) by LND degree. The literal
formula for ED has nonzero S-coefficient \(-2a\), a contradiction.
No normality of the coefficient-extended original ring R is assumed.

## 4. The surviving line gives an original invariant coordinate

In the remaining branch, \(m_s=0\) and \(\sigma\in L\). The whole
return makes \(\theta\) affine and nonconstant. The complete coefficient
identities in
[313](principal-paraboloid-constant-sigma-reducible-line-recognition-pass313-working.md)
give complex \(c,d,\varepsilon\), with \(m=ct+d\ne0\), and
\(y+c\theta/2\in L\). Its actual auxiliary LND is
\[
P_0=aN-(NX)E,\qquad [E,P_0]=0,\qquad
P_0(Y,Z,W)=\tau_0(-c/2,d,X+\varepsilon),\quad
0\ne\tau_0=aN\theta\in L.
\tag{11}
\]
Here N is extended by Nu=0. The construction makes P0 a derivation of
the original ring, not merely its generic coefficient extension.

If \(c\ne0\), set
\(U_0=Z+2dY/c\), \(V_0=W+2(X+\varepsilon)Y/c\).
If \(c=0\), then \(d\ne0\), and set
\(U_0=Y\), \(V_0=W-(X+\varepsilon)Z/d\).
Both are actual polynomial frames with explicit triangular inverses.
In either case
\[
\ker_{\mathcal B}P_0=S=\mathbb C[X,U_0,V_0],\qquad E(S)\subset S.
\tag{12}
\]
The remaining coordinate need not be a slice of P0. The restriction
\(E_0=E|_S\) is nonzero, \(E_0X=a\ne0\), and \(E_0^2X=0\).
Divide its three coefficients by their gcd g. Since g divides the
invariant a, LND degree gives \(E_0g=0\). The resulting derivation D
is an irreducible LND of S with \(DX\ne0\), \(D^2X=0\).

The exact characteristic-zero three-variable theorem
[Dasgupta--Gupta, Theorem4.8](https://arxiv.org/html/1701.03635v1)
then gives an invariant coordinate Q0 of S, and therefore of the
original four-ring. No slice for E0 or D is required. Finally, the
original slice u makes \(A\cong\mathcal B/(u)\) affine and regular.
With Q0 an actual fixed coordinate,
[Bhatwadekar--Gupta--Lokhande, Theorem3.5](https://arxiv.org/html/1501.01438v1)
gives (7). These precise applications, including the primitive-division
gate, are part of313.

## 5. Scope and evidence boundary

The direct classification and endpoint sources above were fully read
before this composition. In particular,323 excludes all genuine conics
without needing the conditional slice-speed or generic-plane conclusions
of316 through320. The independent zero-constant reciprocal proof320
remains valid but is unnecessary for the shortest exhaustive argument.

This synthesis concerns reducibility in \(L[U,P,V]\), not a claim that
every cubic surface over an algebraic closure is reducible. The generic
line O has transcendence degree one over L; the formal monic surface has
dimension two. A projected plane return was obtained only after selecting
a monic factor and using the actual unit-gradient identity in (9).

The irreducible H0 case is outside this theorem. So are the zero-coupling
branch, another full initial kernel, and entry from an arbitrary1222
frame. The conclusion is recognition for the supplied actual reducible
chart, not unrestricted cancellation or a novelty assertion.

No saved checker was executed, imported, compiled, or rerun in preparing
this note. Its conclusion is a composition of the retained mathematical
proofs, not a claim of formal proof certification by their finite controls.
