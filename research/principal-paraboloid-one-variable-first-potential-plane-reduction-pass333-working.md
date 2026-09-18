# A centered plane reduction for a one-variable first potential

Working result: retain the actual principal chart264 with \(k=s\) and
\(n_s=0\), and write \(n=f(t)\) in the exact coefficient constant field.
A coefficient-field centering gives explicit third and fourth potentials.
When \(\ell_s\ne0\), these give a whole polynomial-plane presentation and
a quartic primitive with its unit cofactor retained.

If \(f''\ne0\) and \(\ell_{ss}\ne0\), the selected plane equation must
be a line. All three original intrinsic generators are then affine in
the generic line parameter. For the concrete remaining case
\(f=g t^2\), \(g\in\mathbb C^*\), the alternative \(\ell_{ss}=0\)
reduces to an explicitly constrained quadratic plane primitive.
These are necessary reductions, not recognition of either remaining case.

No arbitrary \(k,n\) normalization, rationality of the coefficient field,
or ambient-coordinate status of the centered first function is assumed.

## 1. Actual inputs and exact constants

Retain every actual hypothesis of the fully read
[264](principal-one-affine-paraboloid-chart-pass264-working.md)
and the fourth-potential conclusion of the fully read
[296](principal-paraboloid-fourth-potential-gradient-minors-pass296-working.md):
\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=A[u],\quad E=\partial_u,\quad
\deg_E(X,Y,Z,W)=(1,2,2,2),\quad a_0=EX\ne0,\\
I_{\mathrm{initial}}=(\mathsf X^2\mathsf Z-\mathsf Y^2)
\text{ is the full weighted initial kernel},\\
L=\operatorname{Frac}\ker_A N,\quad [L:\mathbb C(t,s)]<\infty,
\quad Nv=1,\quad K=\operatorname{Frac}A=L(v),\\
K=\mathbb C(y,z,w),\quad
L[y,z,w]=L[y,\sigma,\theta]=L[v]=:O,\quad
J(X)=-a_0^4\in L^*.
\end{gathered}
\tag{1}
\]
The derivation N is the selected leading part of the literal Z-partial.
The exact coefficient partials commute and fix v. The original E kills
all coefficient functions and intrinsic intercepts.

Assume
\[
k=s,\qquad n_s=0,\qquad
\mathbb F:=\ker_L\partial_s,\qquad n=f\in\mathbb F.
\tag{2}
\]
The field \(\mathbb F\) is finite over \(\mathbb C(t)\), and its exact
t-derivative has constant field \(\mathbb C\). Writing \(f(t)\) means
membership in this finite field, not membership in \(\mathbb C(t)\).
Primes below mean this derivative on \(\mathbb F\).

The complete first two potentials and literal actual map are
\[
\begin{aligned}
z&=2ty+\sigma^2+\theta+f,&
w&=\ell-2\sigma y-f'\sigma,\\
Y&=y+\sigma X+tX^2,&
Z&=z+(2t\sigma+s)X+t^2X^2,&
W&=w+\theta X+sX^2 .
\end{aligned}
\tag{3}
\]
All original scalar coefficients, not just the first two potentials,
remain hypotheses throughout.

## 2. The exact third and fourth potentials

For independent formal variables \(U,P,V\), the third polynomial is
\[
\mathcal H
=U^2+f'U+\frac{f''}{2}P^2-\ell_tP-\ell_sV,
\qquad \mathcal H(y,\sigma,\theta)=h\in L .
\tag{4}
\]
Here264's polynomial \(F(P,V)\) is \(f'P\); its formal V-derivative
vanishes, and the coupling \(m=k_s\) is one.

Consequently296's corrected fourth gradient specializes to
\[
\begin{aligned}
Q_U&=(f''+2\ell_s)P-\ell_t,\\
Q_P&=(f''+2\ell_s)U+\frac{f'''}2P^2
       -\ell_{tt}P-\ell_{ts}V+f'\ell_s-h_t,\\
Q_V&=-\ell_{ts}P-\ell_{ss}V-h_s .
\end{aligned}
\tag{5}
\]
Integrating these formal polynomial derivatives gives
\[
\begin{aligned}
Q={}&\bigl((f''+2\ell_s)P-\ell_t\bigr)U+\frac{f'''}6P^3\\
&-\frac{\ell_{tt}}2P^2-\ell_{ts}PV-\frac{\ell_{ss}}2V^2
 +(f'\ell_s-h_t)P-h_sV,\\
Q(y,\sigma,\theta)&=q_0\in L .
\end{aligned}
\tag{6}
\]
Each coefficient derivative here holds the formal \(U,P,V\) fixed.
The level follows from the complete linear X-coefficient, and the
evaluated two-gradient minors generate O by296. These are not conclusions
about an arbitrary formal map.

Put
\[
p=f'/2,\qquad g=f''/2,\qquad
x=y+p,\qquad \bar h=h+p^2 .
\tag{7}
\]
This is an affine change over L of the first intrinsic function only.
No actual coordinate change \(Y\mapsto Y+p\) is inferred from it.
The complex-p case is treated by an explicit actual translation below.
The first three levels become
\[
\begin{aligned}
z&=2tx+\sigma^2+\theta+f-tf',&
w&=\ell-2\sigma x,\\
x^2+g\sigma^2-\ell_t\sigma-\ell_s\theta&=\bar h .
\end{aligned}
\tag{8}
\]
Translate the formal U in (6) by \(-p\) and remove its formal constant
\(p\ell_t\). The centered fourth polynomial is exactly
\[
\boxed{
Q_c=\bigl(2(g+\ell_s)P-\ell_t\bigr)U+\frac{g'}3P^3
 -\frac{\ell_{tt}}2P^2-\ell_{ts}PV-\frac{\ell_{ss}}2V^2
 -\bar h_tP-\bar h_sV .}
\tag{9}
\]
Indeed \(\bar h_t=h_t+2pg=h_t+pf''\). Thus
\(Q_c(x,\sigma,\theta)=q_0-p\ell_t\in L\).
The formal translation has determinant one, so the unit-minor conclusion
is unchanged. Its coefficient dependence causes no lost derivative:
the translation is applied after the full primitive (6) is derived.

## 3. A genuine plane primitive when \(\ell_s\ne0\)

Assume \(\ell_s\ne0\), and use the exact coefficient parameter
\[
r=\ell,\qquad s=H(t,r),\qquad H_r=1/\ell_s\ne0,\qquad
\mathcal L=H_r\bar h .
\tag{10}
\]
The field L is finite over \(\mathbb C(t,r)\).
The new derivatives are
\(\partial_r=H_r\partial_s\) and
\(\partial_t^{\mathrm{new}}=\partial_t^{\mathrm{old}}+H_t\partial_s\).
They commute, their r-constant field is still \(\mathbb F\), and their
t-derivative on \(\mathbb F\) is unchanged. In particular \(g_r=0\).

Solving the third level gives
\[
\theta=H_r(x^2+g\sigma^2)+H_t\sigma-\mathcal L,\qquad
O=L[x,\sigma].
\tag{11}
\]
The latter is equality of polynomial rings inside K, not merely equality
of fraction fields. Multiplying (9) by \(H_r\), substituting (11), and
removing a formal constant gives the complete plane polynomial
\[
\boxed{\begin{aligned}
\Phi(U,P)={}&\frac{H_{rr}}2(U^2+gP^2)^2
 +H_{tr}(U^2+gP^2)P+\frac{H_{tt}}2P^2\\
&+2(1+gH_r)UP+H_tU+\frac{H_rg'}3P^3\\
&-\mathcal L_r(U^2+gP^2)-\mathcal L_tP,\qquad
\Phi(x,\sigma)=q_1\in L .
\end{aligned}}
\tag{12}
\]

Here is an explicit coefficient-change check. The old partials obey
\[
\begin{aligned}
\ell_t&=-H_t/H_r,& \ell_s&=1/H_r,\\
\ell_{tt}&=-H_{tt}/H_r+2H_tH_{tr}/H_r^2-H_t^2H_{rr}/H_r^3,\\
\ell_{ts}&=-H_{tr}/H_r^2+H_tH_{rr}/H_r^3,&
\ell_{ss}&=-H_{rr}/H_r^3 .
\end{aligned}
\tag{13}
\]
Using \(\bar h=\mathcal L/H_r\), the difference between the substituted
\(H_rQ_c\) and (12) is the coefficient-field constant
\(\mathcal L\mathcal L_r/H_r-\mathcal L^2H_{rr}/(2H_r^2)\).
This proves (12) without suppressing coefficient-level derivatives.

The substituted plane gradient is a unit ideal: the V-coefficient of
the centered third relation is the unit \(-\ell_s\), and the two
plane derivatives are unit multiples of its gradient minors with \(Q_c\).
Hence, if G is the full irreducible equation of \(L[x,\sigma]=L[v]\),
\[
\Phi-q_1=\eta G+G^2R,\qquad
\eta\in L^*,\quad R\in L[U,P].
\tag{14}
\]
The degree and top facts used in corrected301 and330 still apply:
\(\deg G=\max(\deg_vx,\deg_v\sigma)\), and its top homogeneous form is
a power of an L-linear form. In particular \(\Phi\) is not constant.

## 4. A line frontier when \(gH_{rr}\ne0\)

Suppose \(g\ne0\) and \(\ell_{ss}\ne0\), equivalently \(gH_{rr}\ne0\).
The exact quartic top in (12) is
\[
\Phi_4=\frac{H_{rr}}2(U^2+gP^2)^2 .
\tag{15}
\]
Over an algebraic closure of L this has two distinct linear factors,
each with multiplicity two. It is not a fourth power.

Equation(14) excludes selected degree three because \(G^2R\), if
nonzero, would have degree at least six, while \(R=0\) would leave
degree three. Selected degree four would make \(\Phi_4\) proportional
to the pure fourth-power top of G. Selected degree two would require
R to be a nonzero constant, also making \(\Phi_4\) a fourth power.
Both are impossible. The only possible degree is one.

The squared top of this line divides (15), so its equation is
\[
x=\alpha\sigma+\beta,\qquad
\alpha^2=-g,\quad \alpha\in\mathbb F^*,\quad \beta\in L .
\tag{16}
\]
Indeed a line with top P cannot divide (15). Its slope lies in L;
differentiating \(\alpha^2=-g\) in r gives \(\alpha_r=0\), so
\(\alpha\in\mathbb F\). If \(-g\) has no square root in that exact
field, this branch is already impossible.

The whole return makes sigma affine in v. The quadratic terms in (11)
cancel because \(\alpha^2+g=0\), so theta is affine as well. Since
\(y=x-p\), all three original intrinsic generators are affine:
\[
\deg_v\sigma=1,\qquad \deg_vy=1,\qquad \deg_v\theta\le1 .
\tag{17}
\]
This is not ambient recognition or the reducible-surface situation324.
When \(\ell_s\ne0\), the centered third relation is linear in V and
has an irreducible quotient \(L[U,P]\), regardless of (16).

## 5. The remaining quadratic plane framework for complex quadratic f

Now suppose \(g\in\mathbb C^*\). Complex constant translations reduce
\(f=g t^2+f_1t+f_0\) to \(f=g t^2\), if desired: take
\(Y^*=Y+f_1/2\), \(Z^*=Z-f_0\), and keep X,W.
The literal formulas give \(k^*=s,n^*=g t^2,\ell^*=\ell\).
These translations and their inverses preserve the actual leading data.
They do not remove the nonzero quadratic coefficient g.

The case \(\ell_{ss}\ne0\) has already reduced to (16), now with
\(\alpha\in\mathbb C^*\). Suppose instead that
\(\ell_s\ne0,\ell_{ss}=0\). Then \(H_{rr}=0\).
If \(H_{tr}\ne0\), the exact cubic top of (12) is
\(H_{tr}P(U^2+gP^2)\), a product of three distinct linear forms.
It is neither the pure cubic needed for selected degree three nor
divisible by a squared line needed for selected degree one.
Selected degree two is impossible in a cubic by(14).
Therefore \(H_{tr}=0\), and exact constants give
\[
H=c r+d(t),\qquad c\in\mathbb C^*,\quad d\in\mathbb F .
\tag{18}
\]
The plane primitive has degree at most two:
\[
\Phi=-\mathcal L_r U^2+2(1+gc)UP+
       (d''/2-g\mathcal L_r)P^2+d'U-\mathcal L_tP .
\tag{19}
\]
If its degree is two, the unit-cofactor identity and the pure top of G
force its binary quadratic top to be a square. If its degree is at
most one, its quadratic top vanishes. In both cases,
\[
g(\mathcal L_r)^2-\frac{d''}{2}\mathcal L_r-(1+gc)^2=0 .
\tag{20}
\]
Because \(g\ne0\), this is a nonzero polynomial over \(\mathbb F\).
Thus \(\mathcal L_r\) is algebraic over \(\mathbb F\); characteristic
zero and differentiation of its minimal polynomial give
\((\mathcal L_r)_r=0\). Consequently
\[
\boxed{\mathcal L=b(t)r+e(t),\quad b,e\in\mathbb F,\qquad
g b^2-\frac{d''}{2}b-(1+gc)^2=0 .}
\tag{21}
\]
No integration through a presumed rational coefficient field was used.
The cases \(b=0\) and \(1+gc=0\) have not been discarded.
The selected plane equation has degree at most two; the complete
remaining scalar and actual ring conditions still apply.

## 6. Scope, recovered affine case, and unresolved branches

For arbitrary \(f\in\mathbb F\), equations(4)--(12) are exact.
The whole plane reduction requires \(\ell_s\ne0\); no division by
\(\ell_s\) is made or conclusion asserted when it vanishes.
For nonzero \(g=f''/2\), (16)--(17) settle a necessary degree frontier
when \(\ell_{ss}\ne0\). Equations(18)--(21) additionally assume
g is complex nonzero.

If \(f''=0\), exact constants give \(f=f_1t+f_0\) with
\(f_0,f_1\in\mathbb C\). The actual translations
\(Y^*=Y+f_1/2,\ Z^*=Z-f_0\), with X,W fixed, give \(k^*=s,n^*=0\)
and \(\ell^*=\ell\). The supplied normalized-family recognition
[330](principal-paraboloid-normalized-potential-family-recognition-pass330-working.md)
then applies with its retained working dependencies.
This actual affine case is separate from the coefficient-field
centering \(x=y+f'/2\) for nonlinear f.

Neither the affine-generator alternative (17) nor the quadratic
primitive (19)--(21) is declared recognized or realized here.
In particular the concrete nonzero quadratic \(n=g t^2\) is not
claimed removable by the constant translations. The general
\(\ell_s=0\) sector for nonlinear f remains outside this plane argument.

The complete direct sources264,296,330,301 and its mandatory correction
were read before this derivation. A fresh unsaved symbolic calculation
checked all three gradients in(5), the centered primitive(9), and the
complete coefficient transformation(12) with arbitrary jets. Those
identities supplement, not replace, the exact-field and cofactor proofs.
No saved checker was executed, imported, compiled, or rerun by this
author. No earlier proof, checker, canonical index, or ledger was edited.
