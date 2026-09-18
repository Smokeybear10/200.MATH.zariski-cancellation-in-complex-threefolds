# A pure-power leading normalization in every minimal dense three-good frame

For an actual dense three-good frame whose minimum last-coordinate
time degree is \(m\ge2\), the first relation among its coordinate
initials has weighted degree exactly \(m+1\). An actual constant
reframing of the goods and a polynomial shear of the last coordinate
put that relation in the form \(XW-\gamma Y^{m+1}\), with
\(\gamma\in\mathbb C^*\).

The proof extends the multiplicity and invariant-growth argument133
to weights \((1,1,1,m)\). The actual generic-line and first-tail
results139/145 then force the remaining binary leading form to be
a pure power over \(\mathbb C\). The conclusion is a normalization
of leading data, not an invariant correction, a polynomial-kernel
recognition theorem, or an arbitrary-coordinate entry theorem.

## 1. Actual assumptions and the minimum

Assume
\[
\begin{gathered}
B=\mathbb C[x_1,x_2,x_3,W]=A[u],\qquad E=\partial_u,\qquad A=\ker E,\\
E^2x_i=0,\qquad a_i=Ex_i,\qquad
\operatorname{trdeg}_{\mathbb C}\mathbb C(a_1,a_2,a_3)=2,\\
H(a_1,a_2,a_3)\ne0
\quad\text{for every nonzero homogeneous }
H\in\mathbb C[T_1,T_2,T_3].
\end{gathered}
\tag{1}
\]
The four displayed generators are actual polynomial coordinates.
The global slice \(u\) is not assumed to be one of those coordinates.
There is no a priori bound on the last coordinate's time degree.

Keep the complex polynomial good ring fixed and define
\[
\mu=\min_{C\in\mathbb C[x_1,x_2,x_3]}\deg_E(W+C).
\tag{2}
\]
This is an attained nonnegative integer: the set is nonempty, and
each \(W+C\) is a nonzero actual coordinate, with an elementary
polynomial inverse. Assume \(\mu\ge2\). First replace \(W\) by
one minimizing shear and rename it, so that \(m=\deg_EW=\mu\).
Only this existence of a minimum is needed, not a degree bound for
the initial minimizing polynomial.

The selected partial \(T=\partial_W\), holding the goods fixed,
is unchanged by every such shear. It is also unchanged by any
invertible constant linear change among the goods. The intrinsic
data below therefore remain the same throughout the proof.[^1]

The actual cofactor and leading-derivation constructions give
\[
\begin{gathered}
T(A)\subset A[u]_{\le2},\qquad T(u)\in A[u]_{\le2},\qquad
\deg_E(Tf)\le\deg_Ef+2\quad(Tf\ne0),\\
N=[u^2]T|_A\in\operatorname{LND}(A)\setminus\{0\},\qquad
N(a_i)=0,\qquad S=\ker_A N,\qquad L=\operatorname{Frac}S,\\
\operatorname{trdeg}_{\mathbb C}S=2,\qquad
\operatorname{Frac}A=L(v_0),\qquad A_L=L[v_0].
\end{gathered}
\tag{3}
\]
The degree-shift bound includes the coefficient on \(u\), not just
the restriction to \(A\). It has no last-coordinate degree
assumption.[^2] No affine-plane presentation for \(S\) is needed
in this note.

## 2. The full initial kernel has height one

Write \(x_i=b_i+a_i u\), with \(b_i\in A\), and
\(W=\sum_{j=0}^m c_j u^j\). Thus
\(c_m=E^mW/m!\in A\setminus\{0\}\) is the ordinary coefficient
of \(u^m\), not the unnormalized iterate \(E^mW\).

In \(T(W)=1\), the coefficient of \(u^{m+2}\) is exactly
\(N(c_m)\). The terms from \(T(u)\) have degree at most \(m+1\);
the lower \(c_j\) contribute degree at most \(m+1\) as well.
Consequently \(c_m\in S\).

Give the independent source variables
\((\mathsf X_1,\mathsf X_2,\mathsf X_3,\mathsf W)\) weights
\((1,1,1,m)\). With a new indeterminate \(\eta\), form the actual
coordinate-initial map
\[
\begin{gathered}
\theta:\mathbb C[\mathsf X_1,\mathsf X_2,\mathsf X_3,\mathsf W]
 \longrightarrow S[\eta],\\
\theta(\mathsf X_i)=a_i\eta,\qquad
\theta(\mathsf W)=c_m\eta^m,\qquad
\ker\theta=(F),\\
F\text{ irreducible and weighted homogeneous},\qquad d=\operatorname{wt}F.
\end{gathered}
\tag{4}
\]
Here is why the kernel assertion is exact. The three good images
are algebraically independent: separating powers of \(\eta\)
would turn a relation into a homogeneous complex relation among
the \(a_i\), forbidden by (1). Thus the image has transcendence
degree at least three. Its inclusion in \(S[\eta]\) gives degree
at most three. The kernel is therefore a height-one prime in the
polynomial UFD and is principal. The grading makes its irreducible
generator weighted homogeneous.

The generator \(F\) involves \(\mathsf W\), since the good images
have no relation. In characteristic zero,
\(F_{\mathsf W}\ne0\) and \(F\nmid F_{\mathsf W}\), as the latter
has smaller \(\mathsf W\)-degree.

These are the full kernel and the full algebra of the four
coordinate initials. No claim that those initials generate
\(\operatorname{gr}_E B\) is used.

## 3. Exact differentiation detects the multiplicity

Let \(P\) be a nonzero complex polynomial in the four source
variables, with positive weighted degree \(M\) and top part \(P_M\).
Suppose its exact \(F\)-multiplicity is \(k\ge1\):
\[
\begin{gathered}
P_M=F^kG,\qquad F\nmid G,\\
\partial_{\mathsf W}^kP_M
 \equiv k!\,G(F_{\mathsf W})^k\pmod F,\\
\deg_E\bigl(T^kP(x_1,x_2,x_3,W)\bigr)=M-mk,\\
\deg_EP(x_1,x_2,x_3,W)\ge M-(m+2)k .
\end{gathered}
\tag{5}
\]
The congruence follows by the product rule: modulo \(F\), each
of its \(k\) factors must be differentiated exactly once.
The resulting product is nonzero modulo the prime ideal \((F)\).
Its image under \(\theta\) is therefore nonzero.

Differentiating \(k\) times in the last source variable lowers
weighted degree by exactly \(mk\) on this nonzero top part.
Every lower weighted part contributes at most \(M-mk-1\), if it
survives differentiation. Thus its evaluated \(u^{M-mk}\)
coefficient cannot cancel. Because the four coordinates are actual,
source differentiation is exactly the actual operation \(T^k\).
This proves the degree equality in (5), including nonvanishing.
Iterating the all-ring shift bound (3) gives the final inequality.
This is the derivative-multiplicity mechanism133 with its weight
drop \(2\) replaced by \(m\).[^3]

## 4. Invariant growth excludes degree \(m+2\)

For any nonconstant \(a\in A\), let \(P\) be its unique polynomial
expression in the original coordinates and \(M>0\) its weighted
degree. Since \(\deg_Ea=0\), its top \(u^M\) coefficient vanishes.
Hence \(P_M\in(F)\). Using its exact multiplicity \(k\ge1\),
equation (5) gives
\[
kd\le M\le(m+2)k.
\tag{6}
\]
There are nonconstant invariants, so \(d\le m+2\).

Suppose \(d=m+2\). Equality holds throughout (6), and \(G\)
has weight zero. Positivity of all four source weights forces
\(G\in\mathbb C^*\). Thus every nonconstant invariant has highest
weighted part a complex scalar times a power of \(F\).

Let \(\mathcal F_MA\) be the invariants whose original weighted
degree is at most \(M\). Their top-part map shows that each
successive quotient has dimension at most one, and can be nonzero
only at weights divisible by \(d\). Thus
\[
\begin{gathered}
\dim_{\mathbb C}\mathcal F_MA\le\lfloor M/d\rfloor+1,\\
\binom{j+3}{3}\le\dim_{\mathbb C}\mathcal F_{Dj}A
\le\lfloor Dj/d\rfloor+1\qquad(j\ge0).
\end{gathered}
\tag{7}
\]
For the second line choose three algebraically independent
invariants and let \(D>0\) bound their weighted degrees. Their
monomials of total exponent at most \(j\) are independent and
belong to \(\mathcal F_{Dj}A\). The cubic lower bound contradicts
the linear upper bound for large \(j\).
Consequently \(d\le m+1\). This argument needs neither a finite
initial generating set for \(A\) nor a subduction termination claim.

## 5. Minimality leaves one mixed relation and an actual shear

Because \(F\) involves \(\mathsf W\), one has \(d\ge m\).
For \(m\ge2\), the inequality \(d\le m+1<2m\) makes \(F\)
linear in \(\mathsf W\).

If \(d=m\), its coefficient is a nonzero complex constant,
and after scaling \(F=\mathsf W-J_m(\mathsf X)\), with
\(J_m\) homogeneous of degree \(m\). Then
\(c_m=J_m(a)\), so the actual shear \(W-J_m(x)\) has
time degree less than \(m\). Its inverse is polynomial and it
fixes the good ring, contradicting \(m=\mu\).

Therefore the unique initial generator has the form
\[
\begin{gathered}
d=m+1,\qquad
F=L_1(\mathsf X)\mathsf W-H_{m+1}(\mathsf X),\\
L_1\ne0\text{ complex linear},\qquad
H_{m+1}\text{ complex homogeneous},\qquad
\gcd(L_1,H_{m+1})=1,\\
L_1(a)c_m=H_{m+1}(a).
\end{gathered}
\tag{8}
\]
The gcd assertion follows from irreducibility of \(F\).

Choose an invertible constant matrix on the three goods whose
first row is \(L_1\), and call the resulting actual coordinates
\((X,Y,Z)\). Its inverse is the inverse constant matrix.
Write the transformed homogeneous polynomial as
\[
\begin{gathered}
H_{m+1}(X,Y,Z)=XQ_m(X,Y,Z)+B_{m+1}(Y,Z),\\
Q_m\text{ homogeneous of degree }m,\qquad B_{m+1}\ne0,\\
W'=W-Q_m(X,Y,Z),\qquad W=W'+Q_m(X,Y,Z).
\end{gathered}
\tag{9}
\]
The nonzero binary remainder follows from \(X\nmid H_{m+1}\).
This is an actual elementary change of polynomial coordinates,
not a localization at \(X\).

Put \(s=EX,\ t=EY,\ b=EZ\), and let \(c'_m\) be the coefficient
of \(u^m\) in \(W'\). The leading relation becomes
\(s c'_m=B_{m+1}(t,b)\).
Its right side is nonzero: it is a nonzero homogeneous complex
polynomial in the transformed good speeds, whose density survives
the invertible constant matrix. Also \(s\ne0\).
Thus \(c'_m\ne0\) and \(\deg_EW'=m\).
The constant good change preserves the good ring, and the shear
preserves its set of possible last-coordinate degrees, so the
minimum remains exactly \(m\).

The selected partial still kills all three goods and takes value
one on \(W'\), hence is the same \(T\). In particular \(N,S,L\)
are unchanged. Rename \(W'\) as \(W\) and \(c'_m\) as \(c_m\).

## 6. The generic first tail forces a complex pure power

Use the actual dense chart139 for this new selected first good:
\[
\begin{gathered}
\tau=t/s,\qquad \rho=b/s,\qquad
L/\mathbb C(\tau,\rho)\text{ finite separable},\\
Y=y+\tau X,\qquad Z=z+\rho X,\qquad
A_L=L[v],\qquad L[y,z]=L[v],\\
W=\sum_{j=0}^m w_jX^j,\qquad
f_m=w_m=c_m/s^m=B_{m+1}(\tau,\rho).
\end{gathered}
\tag{10}
\]
The coefficient conversion follows by substituting \(X=b_X+su\);
the leading \(X^m\) coefficient is \(c_m/s^m\). Homogeneity
of degree \(m+1\) supplies the last equality from (9).
There is no factorial in that equality.

For formal independent \(U,V\), the exact signed first tail is
\[
\begin{gathered}
\Phi(U,V)=-\sum_{j=0}^m
\sum_{i+k=j+1}
\frac{\partial_\tau^i\partial_\rho^k f_j}{i!\,k!}U^iV^k-f_{-1},\\
\Phi_{m+1}(U,V)=-B_{m+1}(U,V),\qquad
\Phi\in L^*g,\qquad
\ker(L[U,V]\longrightarrow L[v])=(g).
\end{gathered}
\tag{11}
\]
Only \(j=m\) contributes total degree \(m+1\). The Taylor
polynomial of order \(m+1\) of the complex homogeneous
\(B_{m+1}(\tau,\rho)\) is precisely \(B_{m+1}(U,V)\).
Thus that top part is nonzero. The exact association
\(\Phi\in L^*g\) is the actual first-tail theorem145, not
an inference that a selected factor has the same top part as
an arbitrary formal relation.[^4]
In particular \(\deg g=m+1\).

For completeness, the leading form of \(g\) is a pure power
by an elementary projective argument. Put
\(D_0=\max(\deg_v y,\deg_v z)\ge1\), and homogenize the
two polynomials to that degree. The map
\[
\mathbb P^1_L\longrightarrow\mathbb P^2_L,\qquad
[v_1:v_0]\longmapsto
[\,v_0^{D_0}y(v_1/v_0):
  v_0^{D_0}z(v_1/v_0):
  v_0^{D_0}\,]
\tag{12}
\]
is defined everywhere: at \(v_0=0\), at least one leading
coefficient is nonzero. Its image is the projective closure
of the curve \(g=0\), since its affine image is the whole
embedded line. Properness makes that image closed.
The only source point mapping to the line at infinity is
\([1:0]\), and its image is \(L\)-rational.
These statements also hold after extending the coefficient field
to an algebraic closure. Hence the zero set of the highest
binary form of \(g\) consists of that one projective point.
That form is a scalar times the \((m+1)\)-st power of its
linear equation.

By (11), the complex binary polynomial \(B_{m+1}\) has the
same property. Factor it into complex linear forms, using that
\(\mathbb C\) is algebraically closed. Two nonassociated complex
linear factors remain nonassociated over \(L\). There can
therefore be only one factor, so
\(B_{m+1}=\gamma M_1^{m+1}\), with
\(\gamma\in\mathbb C^*\) and \(M_1\) a nonzero complex
linear form in \(Y,Z\). No root extraction in \(L\) or
plane-embedding classification theorem is needed.

Make one final invertible constant change in \(Y,Z\), taking
the new \(Y\) to be \(M_1(Y,Z)\), and rename its speed \(t\).
It fixes \(X,W\), the selected partial, and the good ring.
The resulting exact normalization is
\[
\boxed{
\begin{gathered}
B=\mathbb C[X,Y,Z,W]=A[u],\qquad \deg_EW=\mu=m,\\
s=EX,\quad t=EY,\quad c_m=E^mW/m!,\qquad
s\,c_m=\gamma\,t^{m+1},\\
\ker\theta=(\mathsf X\mathsf W-\gamma\mathsf Y^{m+1}),\qquad
f_m=\gamma\tau^{m+1},\quad \tau=t/s .
\end{gathered}}
\tag{13}
\]
The kernel in (13) uses the final coordinate initials and the
same weights \((1,1,1,m)\). All transformations used to reach
it have explicit polynomial inverses.

## 7. Scope and the remaining correction

The result normalizes leading data in an already supplied
actual dense frame. It does not construct such a frame from
an arbitrary sliced fourfold. It also does not assert that
the particular first-tail parameter descends to the base ring,
that the speed determinant is a unit, or that the primitive
selected action has a slice everywhere.

Even in the final frame, \(XW-\gamma Y^{m+1}\) is an actual
polynomial whose highest time coefficient vanishes. This gives
time degree at most \(m\), not membership in \(A\).
The existence of a lower-degree polynomial correction making
it invariant is a further question, not a conclusion of (13).

The constant leading direction is obtained after the specified
reframing and shear. It is not asserted for every unchanged
choice of first good coordinate. Before this normalization,
(8) already implies that its top chart coefficient belongs to
\(\mathbb C(\tau,\rho)\), but it can have a nonconstant rational
tensor direction there.

The restriction \(m\ge2\) is used in \(m+1<2m\). The cases
\(\mu=0,1\) are not being reproved or reopened here.
The all-degree initial argument extends the written quadratic
case133; its derivative and dimension mechanisms are retained
ones, with every changed weight checked above.
No historical novelty, human expert review, formal verification,
or unrestricted cancellation conclusion is claimed.

## Sources

1. [Fixed-good shear invariance and minimum141](dense-shear-minimal-tail-pass141-working.md),
   Sections 1--2 and 4. Actual elementary inverses, unchanged
   selected partial, and the fixed-good minimum. Its complete
   proof was reread; no equality involving a minimum is
   inferred from an unverified formal component.
2. [Actual dense cofactor bound132](dense-three-good-adjoint-degree-pass132.md),
   Sections 2--5, and [the dense all-degree chart139](dense-all-degree-taylor-chart-pass139-working.md),
   Sections 1--7. The all-ring shift bound, intrinsic nonzero
   LND, exact coefficient field, actual localization and whole
   generic line. The relevant source files were read completely.
   The separate affine-plane quotient theorem is not used.
3. [Quadratic initial-relation dichotomy133](three-good-quadratic-cubic-leading-dichotomy-pass133.md),
   Sections 2--4. The full initial kernel, exact derivative
   multiplicity and positive-weight growth argument were
   reread and reproduced with arbitrary \(m\).
4. [Signed negative-tail identities139](dense-negative-tail-relations-pass139-working.md),
   Sections 1--3, and [actual first-tail primitivity145](common-gauss-integrality-tail-primitivity-pass145-working.md),
   Sections 1--8. The exact selected field and actual inverse
   hypotheses are retained. The complete chart139 and theorem145
   were reread; their proof does not identify a merely selected
   factor with the entire first relation.

[^1]: Source 1.
[^2]: Source 2 and its explicit intrinsic-leading inputs.
[^3]: Source 3.
[^4]: Source 4.
