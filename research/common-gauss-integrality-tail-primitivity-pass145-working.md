# Common Taylor integrality forces first-tail primitivity

In the actual dense three-good chart, the first tail is associated to
the selected irreducible curve equation. A common degree-at-infinity
valuation first handles active factors; polynomial integrality then
proves that every factor is active. The same construction shows that
the fixed Taylor coefficients recover the entire intrinsic coefficient field:
\[
L=\mathbb C(\tau,\rho)(f_0,\ldots,f_m,f_{-1}).
\]
These conclusions remove the first-tail factor and missing
coefficient-field gaps in this chart. They do not give global polynomial
descent or solve unrestricted cancellation.

## 1. Retained actual data

Use the actual chart139 and its first two signed negative coefficients.[^1]
In particular,
\[
\begin{gathered}
B=\mathbb C[X,Y,Z,W]=A[u],\qquad E=\partial_u,\qquad
s=EX\ne0,\qquad E^2X=E^2Y=E^2Z=0,\\
F=\operatorname{Frac}A=L(v),\qquad
K=\mathbb C(\tau,\rho)\subset L,\qquad [L:K]<\infty,\\
\tau=EY/s,\qquad \rho=EZ/s,\qquad
Y=y+\tau X,\quad Z=z+\rho X,\\
F(X)=\mathbb C(X,Y,Z,W),\qquad
W=\sum_{j=0}^{m}w_jX^j,\qquad w_j\in F,\\
\ker(L[U,V]\longrightarrow L[v])=(g),\qquad
L[y,z]=L[v],\qquad \Psi(y,z)=v+c,\quad c\in L .
\end{gathered}
\tag{1}
\]
The speed ratios are algebraically independent and the coefficient
extension is separable. The displayed equality of four-dimensional
fields is actual: it follows from the coordinate inverse and the slice
localization. A unit relative Jacobian alone would not supply it.

The fixed peeling coefficients are \(f_0,\ldots,f_m,f_{-1}\in L\).
For an irreducible \(h\mid\Phi\), put
\[
R_h=L[U,V]/(h),\qquad F_h=\operatorname{Frac}R_h,\qquad
y_h=\overline U,\quad z_h=\overline V,\quad v_h=\Psi(y_h,z_h).
\]
The factor is called active if \(v_h\) is transcendental over \(L\).
Persistence141 then gives
\[
Y_h=y_h+\tau X,\qquad Z_h=z_h+\rho X,\qquad W_h\in R_h[X]
\]
with exactly the same fixed coefficients \(f_j,f_{-1}\) and with the
Taylor embedding \(\Theta_h:L\hookrightarrow F_h((X^{-1}))\).
It satisfies
\[
W_h-\sum_{j=0}^{m}X^j\Theta_h(f_j)
       -X^{-1}\Theta_h(f_{-1})
=X^{-2}\bigl(v_h+O(X^{-1})\bigr).
\tag{2}
\]
Here \(O(X^{-1})\) means a formal series in \(X^{-1}F_h[[X^{-1}]]\).
The signs in (2) are the signed remainder convention of139/141.
The selected factor \(g\) is active, with \(v_g=v+c\).

The proof below does not assume that a component has constant field
exactly \(L\), that its source substitution fixes \(K\), or that its
target field equals \(F_h(X)\).

## 2. One abstract field for all active factors

Take an abstract copy \(L^\flat\) of \(L\); write \(a^\flat\) for the
copy of an element \(a\in L\). This is not initially the original
invariant subfield inside the target field. Let \(\varepsilon,\zeta\)
be algebraically independent over \(L^\flat\), and define
\[
\begin{gathered}
\mathcal E=L^\flat(\varepsilon,\zeta),\qquad
S=\sum_{j=0}^{m}f_j^\flat\varepsilon^{-j}
                  +f_{-1}^\flat\varepsilon,\\
\mathsf X=\varepsilon^{-1},\qquad
\mathsf Y=\tau^\flat\varepsilon^{-1},\qquad
\mathsf Z=\rho^\flat\varepsilon^{-1},\qquad
\mathsf W=S+\varepsilon^2\zeta,\\
\mathcal M=\mathbb C(\mathsf X,\mathsf Y,\mathsf Z,\mathsf W).
\end{gathered}
\tag{3}
\]
These four target elements are algebraically independent over
\(\mathbb C\). The first three generate
\(K^\flat(\varepsilon)\); the fourth is affine in the independent
\(\zeta\) with nonzero coefficient. Thus \(\mathcal M\) is an abstract
copy of the actual target rational field in (1).
Also \(\mathcal E=L^\flat(\varepsilon,\mathsf W)\), a finite
extension of \(\mathcal M=K^\flat(\varepsilon,\mathsf W)\).

For each active \(h\), define a substitution into \(F_h((\varepsilon))\),
where the actual \(X\) on that side is \(\varepsilon^{-1}\):
\[
\begin{gathered}
j_h(a^\flat)=\Theta_h(a)=a+O(\varepsilon)\quad(a\in L),\qquad
j_h(\varepsilon)=\varepsilon,\\
j_h(\zeta)=\varepsilon^{-2}
\left(W_h-\sum_{j=0}^{m}\varepsilon^{-j}\Theta_h(f_j)
                   -\varepsilon\Theta_h(f_{-1})\right)
=v_h+O(\varepsilon).
\end{gathered}
\tag{4}
\]
The next section proves that this substitution extends to a field
embedding. In particular it does not presume that
\(\Theta_h(L)\subset F_h(X)\). Only the established formal Laurent
embedding is used.

The values of the target elements are exactly
\[
j_h(\mathsf X,\mathsf Y,\mathsf Z,\mathsf W)
       =(X,Y_h,Z_h,W_h),
\]
because \(\Theta_h(\tau)=\tau+y_h\varepsilon\) and
\(\Theta_h(\rho)=\rho+z_h\varepsilon\).
Using an independently chosen polynomial target curve in place of
this fixed-coefficient substitution would invalidate (4).

## 3. The pulled-back valuation is the same Gauss valuation

Give \(\mathcal E\) the \(\varepsilon\)-adic Gauss valuation
\(\nu\), with residue field \(L^\flat(\overline\zeta)\).
For a nonzero polynomial
\[
P=\sum_{i=0}^{N}\varepsilon^iP_i(\zeta),
\qquad P_i\in L^\flat[\zeta],
\]
let \(i_0\) be the first index with \(P_{i_0}\ne0\).
Equation (4) gives
\[
\operatorname{ord}_{\varepsilon}j_h(P)=i_0.
\]
Indeed its candidate coefficient at that order is obtained from
\(P_{i_0}\) by returning every \(a^\flat\) to \(a\) and replacing
\(\zeta\) by \(v_h\). It is nonzero because \(v_h\) is transcendental
over \(L\). Terms with larger \(i\) cannot contribute to that order.

This proves injectivity on the polynomial ring and hence gives a field
embedding \(j_h:\mathcal E\hookrightarrow F_h((\varepsilon))\).
Taking quotients proves, for every nonzero \(R\in\mathcal E\),
\[
\begin{gathered}
\operatorname{ord}_{\varepsilon}j_h(R)=\nu(R)
       \quad\text{for every active }h,\\
\overline j_h:L^\flat(\overline\zeta)\hookrightarrow F_h,\qquad
\overline j_h(a^\flat)=a,\quad
\overline j_h(\overline\zeta)=v_h .
\end{gathered}
\tag{5}
\]
The residue map is injective for the same transcendence reason.
The argument covers rational functions whose numerator and denominator
each vanish to positive order: valuation and residue are obtained by
canceling their common powers of \(\varepsilon\), not by specializing
a rational expression with an unchecked denominator.

In particular all active factors induce the same valuation on the
single target field \(\mathcal M\). On its polynomial target subring,
\[
\deg_X P(X,Y_h,Z_h,W_h)
 =\deg_X P(X,Y,Z,W)=\deg_E P(X,Y,Z,W)
\tag{6}
\]
for every nonzero \(P\in\mathbb C[X,Y,Z,W]\).
The middle expression is evaluated on the selected actual chart.
Every image in (6) is polynomial in \(X\), and its degree is the
negative of its \(\varepsilon\)-valuation. The last equality uses
\(E=s\partial_X\) with \(s\in F^*\), so degree in \(X\) over \(F\)
equals degree in the original slice \(u\).

## 4. The fixed coefficients recover the whole coefficient field

Let \(L_0=K(f_0,\ldots,f_m,f_{-1})\) and put
\(\mathcal E_0=L_0^\flat(\varepsilon,\zeta)\subset\mathcal E\).
Every coefficient of \(S\) lies in \(L_0^\flat\), so
\(\mathcal M\subset\mathcal E_0\).

At the selected factor, \(j_g(\mathcal M)=F(X)\) by the actual
field equality in (1). Its restricted valuation is precisely the
ordinary \(X\)-infinity valuation, whose residue field is all of \(F\).
On the other hand the residue of \(\mathcal E_0\) is
\(L_0^\flat(\overline\zeta)\), and (5) sends it into
\(L_0(v+c)\subset F\). Inclusion of valued fields induces inclusion
of their residue fields. Therefore
\[
F\subset L_0(v+c)\subset F,\qquad
F=L_0(v+c),\qquad \boxed{\,L=L_0\,}.
\tag{7}
\]
For the last equality, each element of \(L\) is algebraic over \(L_0\)
and lies in the purely transcendental one-variable field \(L_0(v+c)\).
The only such algebraic elements belong to \(L_0\).
For completeness, if a nonconstant rational function in a
transcendental variable were algebraic over its coefficient field,
that variable would be algebraic over the field generated by the
rational function, contradicting transcendence.

The full residue field here is taken at \(X=\infty\), not at \(X=0\).
An initial source-field presentation at zero does not replace the
actual equality \(j_g(\mathcal M)=F(X)\).
This is why noninvertible formal coefficient-cover examples do not
contradict (7).

## 5. Polynomiality makes every actual invariant stationary

Identify the original rational target field with \(\mathcal M\)
using its four actual coordinate generators. For active \(h\), the
restriction of \(j_h\) gives its target embedding
\(\iota_h:F(X)\hookrightarrow F_h(X)\).

Let \(a\in A\setminus\{0\}\).
Because the four original generators are actual polynomial coordinates,
\(a\) has a complex polynomial expression in them.
Its image \(\iota_h(a)\) therefore lies in \(R_h[X]\).
At the selected factor \(a\in F\) has valuation zero.
Equation (5) gives valuation zero on every active factor.
A nonzero polynomial in \(X\) with that valuation has degree zero.
Consequently
\[
\iota_h(A)\subset F_h,\qquad \iota_h(F)\subset F_h .
\tag{8}
\]
The second assertion follows by taking fractions of the nonzero
constant images. This is the point where polynomiality of the actual
invariant expressions is essential; a rational function of \(X\)
can have valuation zero without being constant in \(X\).

We also obtain exact coefficient return, not merely stationarity.
For \(\alpha\in L\), let \(R_\alpha\in\mathcal M\) represent its
original rational target expression.
Its residue under the selected embedding is \(\alpha\).
The selected residue map (5) is the isomorphism
\[
L^\flat(\overline\zeta)\longrightarrow L(v),\qquad
\alpha^\flat\longmapsto\alpha,\quad
\overline\zeta\longmapsto v+c .
\]
Thus the abstract residue of \(R_\alpha\) must be
\(\alpha^\flat\).
Equation (5) sends that same residue to \(\alpha\) on any active \(h\).
By (8), \(\iota_h(\alpha)\) is already constant in \(X\), so it equals
its own residue. We have proved
\[
\iota_h|_L=\operatorname{id}_L .
\tag{9}
\]
This coefficient-return argument can use the full common field
\(\mathcal E\); it does not depend on first invoking (7), the trace
lemma144, or the polynomial primitive-element criterion143.

## 6. There is exactly one active first-tail factor

The identities \(y=Y-\tau X\) and \(z=Z-\rho X\), together with
(9), give
\(\iota_h(y)=y_h\) and \(\iota_h(z)=z_h\).
Apply the \(L\)-embedding \(\iota_h\) to the selected equation
\(g(y,z)=0\). The result is \(g(y_h,z_h)=0\).
Since the evaluation kernel on \(L[U,V]\) is \((h)\),
the irreducible \(h\) divides the irreducible \(g\).
They are associated. Conversely \(g\) is active by (1).
Hence
\[
\boxed{\quad
h\mid\Phi,\ h\text{ irreducible},\
\Psi\bmod h\text{ transcendental over }L
\quad\Longleftrightarrow\quad h\sim g .
\quad}
\tag{10}
\]
The selected factor occurs with multiplicity one, by the gradient
argument139 or active-factor simplicity141.
The earlier conditional compatibility results now apply automatically
to the only active factor, but they are not inputs to the proof of (10).

## 7. A polynomial integrality statement survives on every factor

We now remove the activity hypothesis. Let \(h\) be any irreducible
factor of \(\Phi\). The coefficient Taylor homomorphism
\(L\to L[[h_1,h_2]]\), followed by
\(h_1=y_h\varepsilon,\ h_2=z_h\varepsilon\), is defined independently
of a separating parameter on \(F_h\). Every nonzero coefficient
has a nonzero constant term and therefore maps to a unit of
\(F_h[[\varepsilon]]\).

Define \(W_h\) by the prescribed nonnegative Taylor part.
The equation \(h\mid\Phi\) alone gives (2) as a formal series identity,
with the possibly algebraic \(v_h=\Psi(y_h,z_h)\).
Thus (4) gives a ring homomorphism
\[
L^\flat[\varepsilon,\varepsilon^{-1},\zeta]
       \longrightarrow F_h((\varepsilon)),
\]
and the image of \(\zeta\) lies in \(F_h[[\varepsilon]]\).
No field embedding is asserted here: when activity is not yet known,
the rational extension and noncancellation claim of Section 3
cannot be used.

For each nonzero \(a\in A\), choose its actual complex target polynomial
\(p_a\) and substitute the common expressions (3). The resulting
\(P_a=p_a(\mathsf X,\mathsf Y,\mathsf Z,\mathsf W)\)
is a finite Laurent polynomial in \(\varepsilon\) and a
polynomial in \(\zeta\), with coefficients in \(L^\flat\).
The selected valuation is zero. Because it is the Gauss valuation,
all negative-\(\varepsilon\) coefficients of this finite expression
must vanish identically as polynomials in \(\zeta\). Consequently
\[
\begin{gathered}
P_a\in L^\flat[\varepsilon,\zeta],\qquad
Q_a(T):=P_a(0,T)\in L^\flat[T]\setminus\{0\},\\
\iota_h(a)=p_a(X,Y_h,Z_h,W_h)\in R_h[X]\cap
                   F_h[[X^{-1}]]=R_h,\\
\iota_h(a)=Q_a^\natural(v_h)\in L[v_h].
\end{gathered}
\tag{11}
\]
The notation \(Q_a^\natural\) returns each coefficient
\(\alpha^\flat\) to \(\alpha\).
The equality in the last line follows by taking the constant
\(\varepsilon\)-coefficient of the integral substitution.
Zero invariants map to zero, so all of the image of \(A\) lies
in \(L[v_h]\).
At this stage \(\iota_h:B\to R_h[X]\) is only the polynomial target
evaluation map; it is not presumed injective.

## 8. The three affine identities make every factor active

Put \(t=EY\) and \(b=EZ\). The actual affine-in-time identities give
\[
x_0=X-su\in A,\qquad y_0=Y-tu\in A,\qquad z_0=Z-bu\in A.
\]
Use a subscript \(h\) for their polynomial target images and for
those of \(s,t,b,u\). By (11), all of the speed and intercept images
belong to \(L[v_h]\). Evaluation gives
\[
\begin{gathered}
X=s_hu_h+(x_0)_h,\qquad
Y_h=t_hu_h+(y_0)_h,\qquad Z_h=b_hu_h+(z_0)_h,\\
s_h\ne0,\qquad u_h=\frac{X-(x_0)_h}{s_h}.
\end{gathered}
\tag{12}
\]
If \(s_h=0\), the first identity would make the independent
indeterminate \(X\) equal a coefficient-field element, an impossibility.
Substitute the last expression for \(u_h\) into the other two
identities and compare the coefficient of \(X\) and the constant
coefficient. This gives
\[
\begin{gathered}
\tau=t_h/s_h,\qquad \rho=b_h/s_h,\\
y_h=(y_0)_h-\tau(x_0)_h\in L[v_h],\qquad
z_h=(z_0)_h-\rho(x_0)_h\in L[v_h],\\
R_h=L[y_h,z_h]=L[v_h],\qquad F_h=L(v_h).
\end{gathered}
\tag{13}
\]
The reverse inclusion in the ring equality uses
\(v_h=\Psi(y_h,z_h)\).
By construction \(F_h\) has transcendence degree one over \(L\).
Equation (13) therefore forces \(v_h\) to be transcendental over
\(L\): the factor is active.
This proves activity using the six actual speed and intercept
invariants, not by assuming a component field embedding in advance.
In addition, \(u_h\in R_h[X]\), so the coefficient of \(X\) in (12)
puts \(1/s_h\) in \(R_h=L[v_h]\).
Thus \(s_h\in R_h^*=L^*\), consistently with the later exact
coefficient-return conclusion.

Every irreducible factor of \(\Phi\) is now active, so (10) identifies
each with \(g\). The selected factor is simple by139/141. We conclude
\[
\boxed{\qquad
\Phi\in L^*g,\qquad
L=K(f_0,\ldots,f_m,f_{-1}),\qquad
\deg\Phi=\deg g .
\qquad}
\tag{14}
\]
The active and formerly inactive cases have both been addressed.
In particular the argument rules out repeated residual factors as
well as distinct ones.

## 9. The fixed-good minimum equals the generic curve degree minus one

The earlier fixed-good shear theorem141 proves
\(\min_{P\in\mathbb C[X,Y,Z]}\deg_E(W+P)=\deg\Phi-1\).
The generic projection calculation139 gives
\(\deg g=\max(\deg_v y,\deg_v z)\).
Combining these two retained results with (14) now yields the exact
unconditional equality in the present chart:
\[
\boxed{\quad
\min_{P\in\mathbb C[X,Y,Z]}\deg_E(W+P)
=\deg g-1=\max(\deg_v y,\deg_v z)-1 .
\quad}
\tag{15}
\]
Here the three good coordinates remain fixed. The minimizing shear
is the explicit complex polynomial supplied in141, not a new change
of coordinates over \(L\). At least one of \(y,z\) is nonconstant
because they generate \(L[v]\); hence the right side is nonnegative.
This includes \(m=0\), where both the minimum and \(\deg g-1\)
are zero. The equality does not minimize over arbitrary changes
of the good-coordinate ring.

## 10. Exact remaining scope

The conclusion is first-tail primitivity for the retained actual dense
three-good setup. It does not say that the particular pair
\((\Phi,\Psi)\) is a plane coordinate system; earlier actual examples
already rule out that stronger inference.
Although \(g\) is a coordinate over \(L\) by the classical plane
epimorphism theorem, the present proof does not remove coefficient
denominators or descend that coordinate to the original complex ring.

No invariant ambient coordinate is constructed here, and no argument
puts an arbitrary sliced polynomial fourfold into this three-good
setup. Global polynomial descent and arbitrary coordinate entry remain
open in this investigation. The unconfirmed corrected complex-threefold
cancellation target remains unsolved.

## Sources and verification status

1. [The actual dense chart139](dense-all-degree-taylor-chart-pass139-working.md)
   and [the signed negative-tail identities139](dense-negative-tail-relations-pass139-working.md).
   Exact coefficient field, actual target equality, selected generic
   parameter and remainder signs.
2. [Component persistence141](dense-tail-component-persistence-pass141-working.md).
   The algebraic Taylor embedding and equation (2) for each active
   factor. No inverse-field equality for other factors is assumed.
3. [Trace and compatible-factor results144](closed-tail-field-parallel-fibers-pass144-working.md).
   Context for the gaps removed here, not an input to the direct
   stationarity and coefficient-return proof.
4. [Fixed-good shear minimum141](dense-shear-minimal-tail-pass141-working.md),
   Sections 2--4, and [generic embedded-line degree139](dense-generic-embedded-line-pass139-working.md),
   Section 3. These are the two previously proved inputs to (15).

The Gauss noncancellation and residue comparisons are proved above.
No external valuation classification is invoked. These are working
deductions from the retained actual chart, not a recursive audit of
all earlier reductions, a historical novelty determination, human
expert review, or proof-assistant verification.

[^1]: Sources 1--2. The actual coordinate inverse is used both for
    the full selected target field and for polynomial invariant images.
