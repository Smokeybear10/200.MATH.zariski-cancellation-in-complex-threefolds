# A triangular residue extension cannot occupy an affine-linear projected frame

The standard triangular examples with nontrivial divisor constants do
not automatically extend to actual dense three-good coordinate frames.
This note excludes all constant-affine placements of their two projected
goods on a chart meeting a genuinely nonlinear triangular divisor fiber.
The triangular equation may have arbitrary polynomial dependence on
the base variable. The last original coordinate can have arbitrary
time degree.

The exclusion is conditional on a specified chart identification.
It does not show that every intrinsic action admits that identification,
or rule out arbitrary nonlinear placements of the projected goods.
In particular, it does not prove that all the residue extensions in147
are trivial, nor solve cancellation.

## 1. Actual inputs and the additional triangular-chart hypothesis

Retain the actual dense setup of139/147:
\[
\begin{gathered}
B=\mathbb C[X,Y,Z,W]=A[u],\qquad E=\partial_u,\qquad
E^2X=E^2Y=E^2Z=0,\\
s=EX,\quad \tau=(EY)/s,\quad \rho=(EZ)/s,\qquad
N=[u^2]\partial_W|_A\ne0,\qquad S=\ker_A N .
\end{gathered}
\tag{1}
\]
The speed field has transcendence degree two and no nonzero homogeneous
relation. The retained actual chart conclusions give
\[
\begin{gathered}
B_s=A_s[X],\qquad Y=y+X\tau,\qquad Z=z_0+X\rho,\\
A_s=\mathbb C[y,z_0,w_0]_{s_0},\qquad
\tau,\rho\in\operatorname{Frac}S\text{ algebraically independent},\\
L[y,z_0]=A_L=L[v],\qquad L=\operatorname{Frac}S .
\end{gathered}
\tag{2}
\]
The first two rows of the Jacobian of the actual coordinate map
\((Y,Z,W)\), with \(X\) fixed, cannot lose rank anywhere on this
localized chart. Indeed their completion by the third row has a
unit determinant. This uses the actual polynomial inverse, not a
converse to the Jacobian condition.

Assume additionally that there is an identification of embedded
coefficient rings and actual chart algebras
\[
\begin{gathered}
S=\mathbb C[r,q],\qquad
A_s=\mathbb C[r,t,z]_{h(r,q)},\qquad
q=a(r)z-H(r,t),\\
a\in\mathbb C[r]\text{ nonconstant},\qquad
H\in\mathbb C[r,t],\qquad
0\ne h\in\mathbb C[r,q],\\
a(r_0)=0,\qquad h(r_0,q)\ne0,\\
P(t):=H(r_0,t),\qquad d=\deg P\ge2,\\
y,z_0\text{ are complex affine-linear forms in }r,t,z.
\end{gathered}
\tag{3}
\]
The equality involving \(S\) specifies its inclusion in the chart;
it is not merely an abstract isomorphism of two polynomial rings.
The condition on \(h\) says that the chart meets the generic point
of the divisor \(r=r_0\). The two affine-linear forms have independent
linear parts, since \(y,z_0,w_0\) are actual chart coordinates.

**Claim.** Conditions (1)--(3) are incompatible.

The proof has three cases. The main case supplies a critical point
over an algebraic closure of the generic coefficient field. The other
two cases violate retained generic generation or divisor noncollapse.

## 2. The main case: the projected plane sees both \(t\) and \(z\)

Suppose the restrictions of the two linear parts to the \((t,z)\)
plane have rank two. An invertible constant linear combination of
the two goods, followed by removal of their constant terms, makes
their intercepts
\[
y=t+\alpha r,\qquad z_0=z+\beta r,\qquad
Y=t+\alpha r+Xf(r,q),\quad
Z=z+\beta r+Xg(r,q).
\tag{4}
\]
Here \(\alpha,\beta\in\mathbb C\). The same invertible combination
of the speed ratios gives \(f,g\in K=\mathbb C(r,q)\) with
\(J=f_r g_q-f_q g_r\ne0\). Coordinate-pair rank and the actual
completion property are unchanged. A constant affine change of the
goods does not require a nonlinear change of the original chart.

Work over \(K\), and express \(z=(q+H(r,t))/a\), where \(a=a(r)\).
The rational coordinate change from \((r,t,z)\) to \((r,q,t)\)
has nonzero determinant on \(a\ne0\). With \(X\) fixed, the rows
of the two differentials in the order \((r,q,t)\) are
\[
\begin{pmatrix}
\alpha+Xf_r&Xf_q&1\\
\beta+H_r/a-a'(q+H)/a^2+Xg_r&1/a+Xg_q&H_t/a
\end{pmatrix}.
\tag{5}
\]
These are absolute differentials over \(\mathbb C\), computed before
evaluation at the generic-field point. Organizing coefficients in
\(K\) does not set \(dr\) or \(dq\) equal to zero.
The prime on \(a\) means its one-variable derivative; subscripts on
\(H\) refer to the displayed independent variables \(r,t\).

Define two polynomials in the generic parameter \(t\):
\[
\begin{aligned}
D(t)&=a g_q-H_t f_q,\\
I(t)&=a'(q+H)-aH_r+\alpha aH_t-\beta a^2,\\
F(t)&=I(t)D(t)+a^2 g_r-aH_t f_r .
\end{aligned}
\tag{6}
\]
All their coefficients belong to \(K\).

We next prove that \(F\) is nonconstant. A generic degree comparison
is insufficient when \(H\) has higher-degree terms divisible by
\(r-r_0\); a coefficient valuation at that divisor supplies the
needed argument.

Put \(p=r-r_0\), and write \(a=p^e b(p)\), where \(e\ge1\) and
\(b_0=b(0)\ne0\). Rational functions of \(r,q\) have formal Laurent
expansions in \(\mathbb C(q)((p))\). In the corresponding series
ring with polynomial \(t\)-coefficients,
\[
H=P+O(p),\qquad H_t=P'+O(p),\qquad
I=e b_0(q+P)p^{e-1}+O(p^e).
\]
Here \(H_r\) is polynomial, so its contribution to \(I\) starts
at order at least \(e\). The two affine terms likewise start later.

Write \(F=F_f+F_g\), where
\[
F_f=-H_t(I f_q+a f_r),\qquad
F_g=a(I g_q+a g_r).
\]
Subtracting a complex constant from \(f\) changes none of these
expressions. Since \(J\ne0\), \(f\) is not constant. After that
subtraction, its first Laurent coefficient has the form
\(f_n(q)p^n\), with \(n\ne0\) or \(f_n'(q)\ne0\).
Coefficientwise differentiation gives the first nonzero term of
\(F_f\) at order \(n+e-1\), with coefficient
\[
-b_0P'\bigl(e(q+P)f_n'+n f_n\bigr).
\]
If \(f_n'\ne0\), its \(t\)-degree is \(2d-1\). Otherwise
\(n\ne0\), and its degree is \(d-1\). Both are positive.

If \(g_q=0\), \(F_g=a^2g_r\) is constant in \(t\) and cannot
cancel that nonconstant coefficient. Otherwise let \(m\) be the
first Laurent index of \(g\) for which \(g_m'(q)\ne0\).
There are only finitely many earlier terms. Removing those
\(q\)-constant terms changes \(F\) only by a \(t\)-constant
element of \(K\), namely \(a^2\) times their \(r\)-derivative.
This is a calculation modulo \(K\), not a change to the actual
coordinate frame or to its speed ratios.

For this computation of nonconstant coefficients, \(F_g\) first
appears at order \(m+2e-1\), with coefficient
\[
b_0^2\bigl(e(q+P)g_m'+m g_m\bigr),
\]
whose \(t\)-degree is \(d\). If the orders of the first \(f\)- and
\(g\)-contributions differ, the earlier nonconstant coefficient
survives. If the orders agree, their degrees are distinct:
\(2d-1\) versus \(d\) when \(f_n'\ne0\), and \(d-1\) versus
\(d\) otherwise. They cannot cancel. Thus \(F\notin K\), proving
that \(F(t)\) is nonconstant without a bound on \(\deg_t H\).

Every root \(\theta\) of \(F\) in an algebraic closure \(\overline K\)
satisfies \(D(\theta)\ne0\). When \(f_q=0\), \(D=a g_q\ne0\).
When \(f_q\ne0\), a simultaneous zero would give
\(H_t(r,\theta)=a g_q/f_q\), and hence
\[
F(\theta)=a^2g_r-aH_t(r,\theta)f_r
         =-a^2J/f_q\ne0,
\tag{7}
\]
a contradiction.

Choose such a root and put \(X=-1/D(\theta)\), \(t=\theta\),
\(z=(q+H(r,\theta))/a\). In (5), the second entry of the second row
minus \(H_t/a\) times the first row is
\((1+XD)/a=0\). The first entry of the same row difference is
\[
\beta+\frac{H_r}a-\frac{a'(q+H)}{a^2}-\frac{\alpha H_t}a
 +X\left(g_r-\frac{H_tf_r}a\right)
 =-\frac{F}{a^2D}=0.
\tag{8}
\]
Its third entry is zero identically. The first row has third entry
one, so the rows have rank exactly one at this point.

This is a point of the allowed chart: \(r,q\) retain their generic
values, so every nonzero invariant denominator \(h(r,q)\), and
the denominators of \(f,g\), are nonzero. A ring homomorphism to
\(\overline K\) annihilating all the two-by-two minors proves that
their ideal is proper. No unproved specialization to a complex
closed point is needed. The actual third coordinate cannot complete
this rank-one pair to an invertible Jacobian, contradicting (2).

This main case does not need the chart to meet \(r=r_0\).
It excludes completion even after an arbitrary nonzero invariant
localization, provided the triangular polynomial has the stated
nonlinear specialization at some root of \(a\). The premise that
this divisor survives in the chart is needed in the last case below.

## 3. The remaining projected planes

If the projection of the two-dimensional plane of linear parts onto
the \((t,z)\) plane has rank one, its kernel is the \(r\)-direction.
After another constant invertible combination and removal of constants,
the intercepts are therefore
\[
y=r,\qquad z_0=b t+c z,\qquad (b,c)\ne(0,0).
\tag{9}
\]
Rank zero is impossible because the original two linear parts are
independent.

First suppose \(c\ne0\). On the generic coefficient fiber the full
algebra in (3) is \(K[t]\), whereas
\[
K[y,z_0]=K\!\left[b t+\frac{c(q+H(r,t))}{a}\right].
\]
The displayed generator has degree \(\deg_t H\ge d\ge2\), so it
does not generate \(K[t]\): a nonconstant polynomial in that generator
has degree a positive multiple of \(\deg_t H\), never one. This contradicts
the whole generic line assertion in (2).

Finally suppose \(c=0\), so \(b\ne0\). At the generic point of
\(r=r_0\), let \(k=\mathbb C(q)\). The full fiber specified by
(3) is
\[
k[t,z]/(q+P(t)).
\]
It is nonzero; \(q+P(t)\) is irreducible over \(\mathbb C(q)\).
One elementary proof is that \(q+P(t)\) is prime in
\(\mathbb C[q,t]\), with quotient \(\mathbb C[t]\), and that this
quotient injects \(\mathbb C[q]\) via \(q\mapsto-P(t)\).
Localizing by its nonzero elements retains a nonzero prime quotient.
In particular \(t\) is algebraic over \(k\).

Both projected goods in (9) thus reduce to algebraic elements over
\(k\). But134, applied as in147, requires at least one projected good
to remain transcendental over the coefficient residue field on
every divisor visible in a selected-speed chart. Explicitly,
\((r-r_0)B\cap\mathbb C[X,Y,Z]=0\). If both intercepts were
algebraic, the three original goods would lie in a field of complex
transcendence degree at most two, contradicting that injection.
The condition \(h(r_0,q)\ne0\) ensures that this divisor was not
removed. This completes the third case and the proof.

## 4. What has, and has not, been excluded

The abstract147 controls \(q=r z-t^d\) are instances of this family.
Their nontrivial finite residue constants remain valid examples for
ordinary triangular LNDs. The present argument shows why they cannot
be inserted into the indicated actual dense chart, even after
constant-affine reorientation of its two projected goods.

The general \(H(r,t)\) includes, for example, arbitrary polynomial
shears of the third triangular coordinate, which add a multiple of
\(a(r)\) to the triangular equation. Its higher generic degrees do
not escape the argument: the valuation calculation detects the
nonlinear residual polynomial. The embedded-base premise in (3)
remains necessary. It is not inferred for every arbitrary choice
of \(a,H\); specializations at other roots can enlarge a triangular
kernel if their polynomial in \(t\) becomes constant.

The proof does not assume that the selected speed is one.
The functions \(f,g\) are rational speed ratios, and their denominators
are harmless in the generic critical-point case. No bound on the
time degree of the completing \(W\) enters anywhere.

The two projected goods need not be affine-linear in a polynomial
coordinate system putting a general intrinsic action into triangular
form. An arbitrary polynomial change can destroy precisely that
condition. No triangularization theorem or automatic affine placement
is claimed. Actual nonlinear placements and other intrinsic kernels
remain possible targets.

## Dependencies and verification scope

- [Actual chart139](dense-all-degree-taylor-chart-pass139-working.md),
  Sections 1--3 and 7: the genuine localized inverse, ratio field,
  and whole generic line.
- [Divisor exclusion134](dense-good-speed-divisor-exclusion-pass134.md)
  and [residue bound147](dense-all-degree-divisor-residue-bound-pass147-working.md),
  Section 3: the actual good-ring injection and noncollapse.

The rank calculation and the three-case exclusion are written
algebraic arguments. Finite symbolic controls, if recorded separately,
do not establish their universal quantifiers. The argument is a private
working result awaiting independent human review; no historical
novelty, proof-assistant verification, or cancellation claim is made.
