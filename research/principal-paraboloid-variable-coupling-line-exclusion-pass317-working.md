# Variable transverse coupling is impossible on the reducible projected line

Working result: in the actual reducible-surface projected-line sector
of309, the branch \(m_s\ne0\) is impossible. The proof uses314's
actual normalization, the complete lower factor coefficients, and
the full calibrated determinant. It keeps both projected-line
directions and both possible selected surface factors.

No step divides by \(h'\), the discriminant of h, or a projected
slope before proving that slope nonzero. In particular the constant-h
case is included. This is a conditional exclusion inside the supplied
actual1222 chart, not an unrestricted entry or cancellation theorem.

## 1. Retained actual inputs and the normalized coefficient variables

Retain the actual chart and full determinant of the fully read
[296](principal-paraboloid-fourth-potential-gradient-minors-pass296-working.md),
the reducible projected-line affinity of
[309](principal-paraboloid-reducible-line-affine-generators-pass309-working.md),
and the complete actual normalization of the fully author-read
[314](principal-paraboloid-variable-coupling-hodograph-reduction-pass314-working.md).
In particular
\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=A[u],\qquad E=\partial_u,\qquad
\deg_E(X,Y,Z,W)=(1,2,2,2),\\
I_{\rm initial}=(X^2Z-Y^2),\qquad a=EX\ne0,\qquad
[L:\mathbb C(t,s)]<\infty,\\
O=L[v]=L[\sigma,\theta],\qquad Nv=1,\qquad
y,\sigma,\theta\text{ are affine in }v,\\
J(X)=\det\frac{\partial(Y,Z,W)}{\partial(t,s,v)}
       =-a^4\in L^* .
\end{gathered}
\tag{1}
\]
The formal monic surface \(H-h_0\) is reducible, and its two
evaluated factor coefficients differ by a unit of O, hence by an
element of \(L^*\). These statements survive314's actual reframe,
not merely a coefficient-field substitution.

The normalized coefficient equation is
\[
k^2=2h(t)s,\qquad h\in\mathbb C[t]\setminus\{0\},\quad
\deg h\le2.
\tag{2}
\]
Put \(r=k\). Then t,r are algebraically independent, L is finite
over \(\mathbb C(t,r)\), and
\[
s=\frac{r^2}{2h},\qquad m=\frac hr,\qquad
\partial_{t,\mathrm{old}}
 =\partial_t+\frac{rh'}{2h}\partial_r,\qquad
\partial_{s,\mathrm{old}}=\frac hr\partial_r .
\tag{3}
\]
The unadorned partials below fix the other member of t,r and fix v.
They are the commuting extensions from the rational base to L.
Write \(\mathcal F=\ker_L\partial_r\), finite over \(\mathbb C(t)\).
Its t-derivative has constants exactly \(\mathbb C\).
Integration coefficients in \(\mathcal F\) will not be assumed
rational in t.

Set
\[
\mathfrak d=2hh''-(h')^2\in\mathbb C.
\tag{4}
\]
The constant, linear and quadratic possibilities for h are all
retained, including \(\mathfrak d=0\).

## 2. Literal surface and the degree-labelled affine factor

Use independent formal variables U,P,V. All derivatives in the
following display are the old fixed-s or fixed-t derivatives:
\[
\begin{aligned}
F&=\frac{k_{tt}}2P^2+k_{ts}PV+\frac{k_{ss}}2V^2+n_tP+n_sV,\\
\gamma&=2P+k_t,\qquad g=\frac{\ell-\gamma U-F}{m},\\
H&=U^2+F_PU+F_Vg+H_3(k;P,V)+H_2(n;P,V)
                         -\ell_tP-\ell_sV .
\end{aligned}
\tag{5}
\]
Here \(H_i\) is the full homogeneous Taylor polynomial, with its
factorial denominators. In particular no lower-potential jet is
omitted.

Write
\[
H-h_0=U^2+A_1U+A_0=(U+\mathsf A)(U+\mathsf B),
\qquad A_1=F_P-\gamma F_V/m .
\tag{6}
\]
Since \(m_s=-h^2/r^3\ne0\), the quadratic part of \(A_1\) is
nonzero. As in314, exactly one of the factor coefficients is
quadratic and the other has degree at most one. Label the latter
\(\mathsf B\), without assuming it is the selected factor.

The entire cubic coefficient product fixes its linear part:
\[
\mathsf B=b_PP+b_VV+b_0,\qquad
b_P=\frac{r\mathfrak d}{8h^2},\qquad
b_V=\frac{h'}{4r}.
\tag{7}
\]
Indeed the raw cubic part of \(A_0\) is
\(H_3(k)-(k_{ts}P+k_{ss}V)H_2(k)/m\), and its quotient by
\((A_1)_2\) is \(b_PP+b_VV\). If that cubic part is zero, this
same identity gives zero linear part. Neither \(h'\) nor
\(\mathfrak d\) has been divided by.

Let
\[
\mathcal R=A_0-(A_1-\mathsf B)\mathsf B .
\tag{8}
\]
Factorization makes every coefficient of \(\mathcal R\) vanish.
The surface-level constant \(h_0\) occurs only in its constant
coefficient. We will use all five positive-degree coefficients
of total degree at most two.

## 3. The three quadratic coefficients determine n exactly

Rebuild (5) using the derivative operators (3). The \(V^2\)
coefficient of (8) is
\[
[V^2]\mathcal R
 =\frac{h^2}{2r^3}(r n_{rr}+2n_r)
                  -\frac{3(h')^2}{16r^2}.
\tag{9}
\]
Its vanishing integrates exactly to
\[
n=\frac{r^2(h')^2}{16h^2}+\frac{f(t)}r+j(t),
\qquad f,j\in\mathcal F .
\tag{10}
\]
For completeness, after subtracting the displayed quadratic
particular solution, the differential equation is
\((r^2n_r)_r=0\). Its two integration coefficients are precisely
elements of \(\mathcal F\), so no algebraic-field homogeneous mode
has been discarded.

The \(PV\) coefficient has coefficient \(-2h/r^2\ne0\) on \(b_0\).
After (10), it therefore gives the unique value
\[
b_0=\frac{r^2h'\mathfrak d}{32h^3}
                      +\frac{j'}2+\frac{f h'}{4rh}.
\tag{11}
\]
Substituting this value, the remaining \(P^2\) coefficient is
\[
[P^2]\mathcal R
 =\frac{j''}2+\frac{h}{2r}\left(\frac fh\right)'' .
\tag{12}
\]
The variable r is transcendental over \(\mathcal F\). Thus
\(j''=0\) and \((f/h)''=0\). The exact constant field now gives
\[
q=f/h=q_1t+q_0,\qquad j=j_1t+j_0,\qquad
q_i,j_i\in\mathbb C,
\qquad
n=\frac{r^2(h')^2}{16h^2}+\frac hrq+j .
\tag{13}
\]
At this stage \(q_1\) may be zero. Its nonvanishing will be a
consequence of the actual projected line, not an integration
assumption.

## 4. The two linear coefficients determine ell exactly

For short coefficient displays define
\[
\alpha=\frac{(h')^2\mathfrak d}{128h^4},\qquad
\beta_0=\frac{h'j_1}{4h},\qquad
\gamma_0=\frac{h'q_1}{4}+\frac{q(h')^2}{8h},\qquad
\delta_0=\frac{h^2q^2}{2}.
\tag{14}
\]
These symbols are not projected slopes. After (11)--(13), the
complete linear V coefficient is
\[
[V]\mathcal R
 =-\frac h{r^2}
   \left((r\ell)_r+4\alpha r^3+2\beta_0r+\gamma_0
                                      +\frac{2\delta_0}{r^3}\right).
\tag{15}
\]
Its full solution in L is
\[
\ell=-\alpha r^3-\beta_0r-\gamma_0+\frac{e(t)}r
                                      +\frac{\delta_0}{r^3},
\qquad e\in\mathcal F .
\tag{16}
\]
The remaining P coefficient is exactly
\[
[P]\mathcal R=-\frac hr\left(\frac eh\right)'.
\tag{17}
\]
Hence \(e/h=c\in\mathbb C\). We have proved the full necessary
lower-potential family
\[
\boxed{
\ell=-\frac{r^3(h')^2\mathfrak d}{128h^4}
     -\frac{rh'j_1}{4h}-\frac{h'q_1}{4}
     -\frac{q(h')^2}{8h}
     +\frac{ch}{r}+\frac{h^2q^2}{2r^3}.}
\tag{18}
\]
Equations (9),(11),(12),(15),(17) use every positive-degree
coefficient below the cubic part. The constant coefficient merely
determines the surface level. The derivation did not divide by
\(q_1,j_1,f,e,h'\), or \(\mathfrak d\).

## 5. The unit factor difference gives exactly two line directions

Introduce affine projected variables over L,
\[
S=P+\frac{rh'}{4h},\qquad T=V+q .
\tag{19}
\]
The map \((P,V)\mapsto(S,T)\) is an invertible translation.
Using (11),(13), the full affine factor and factor difference are
\[
\begin{aligned}
\mathsf B&=\frac{r\mathfrak d}{8h^2}S
                           +\frac{h'}{4r}T+\frac{j_1}{2},\\
\mathsf A-\mathsf B
 &=S\left(\frac{2h}{r^2}T-\frac{h'}hS\right)+\frac hrq_1 .
\end{aligned}
\tag{20}
\]
These are formal identities before restriction to the actual line.

Now evaluate at \(P=\sigma,V=\theta\). The two functions
\[
S,\qquad R=\frac{2h}{r^2}T-\frac{h'}hS
\]
are affine in v, and their pair generates \(O=L[v]\): the
linear change from \(S,T\) has nonzero determinant \(2h/r^2\).
By the unit difference, (20) makes \(SR\) constant in v.
If this constant were nonzero, both factors would be units of
\(L[v]\), hence both constant, contradicting whole O-return.
Thus \(SR=0\). The domain O gives exactly one of
\[
\text{I: }S=0,\ T\text{ nonconstant affine};\qquad
\text{II: }R=0,\ S\text{ nonconstant affine}.
\tag{21}
\]
The other factor cannot also be zero, by the same return.
In either case \((\mathsf A-\mathsf B)^{\rm ev}=hq_1/r\).
It is a unit, so
\[
q_1\in\mathbb C^*.
\tag{22}
\]
This argument keeps the constant-h case. Case I is the
\(\sigma_v=0\) direction, and Case II has \(\sigma_v\ne0\).

Because O is a domain, one factor in (6) vanishes identically.
Accordingly the selected first intrinsic generator has one of
the two values
\[
y=-\mathsf B^{\rm ev}-\varepsilon\frac hrq_1,
\qquad \varepsilon=0\ \hbox{or}\ 1.
\tag{23}
\]
The value zero selects the degree-labelled affine factor, while
one selects the quadratic factor. No interchange of these
selections is assumed.

## 6. All four literal maps and the parameter calibration

In Case I take \(p=T\). In Case II take \(p=S\). In either case
\(p\) is nonconstant affine in the original v, so \(Np\in L^*\)
and \(O=L[p]\).

Using (13),(18) in the original first and second potentials,
not only the selected surface equation, gives the following
complete intercepts.

Case I:
\[
\begin{aligned}
\sigma&=-\frac{rh'}{4h},&
\theta&=p-q,\\
y&=-\frac{h'p}{4r}-\frac{j_1}{2}
                         -\varepsilon\frac hrq_1,&
z&=2ty+\frac hrp+j,\\
w&=c+\frac{hp^2}{2r^2}.&&
\end{aligned}
\tag{24}
\]
Case II:
\[
\begin{aligned}
\sigma&=p-\frac{rh'}{4h},&
\theta&=\frac{r^2h'p}{2h^2}-q,\\
y&=-\frac{rh''p}{4h}-\frac{j_1}{2}
                         -\varepsilon\frac hrq_1,&
z&=2ty+p^2+\frac{rh'}{2h}p+j,\\
w&=c+(2\varepsilon-1)pq_1+\frac{p^2r^2h''}{4h^2}.&&
\end{aligned}
\tag{25}
\]
In deriving (24),(25), one substitutes into
\(z=2ty+\sigma^2+k_t\sigma+m\theta+n\) and
\(w=(\ell-(2\sigma+k_t)y-F(\sigma,\theta))/m\).
Thus the W-intercept and its selected-factor dependence are
retained. The cancellation in Case I's w is valid for either
selection.

For all four possibilities the full original coordinates remain
\[
\begin{aligned}
Y&=y+\sigma X+tX^2,\\
Z&=z+(2t\sigma+r)X+t^2X^2,\\
W&=w+\theta X+\frac{r^2}{2h}X^2 .
\end{aligned}
\tag{26}
\]
The coefficient and parameter change from \((t,s,v)\) to
\((t,r,p)\) has inverse Jacobian \(r/(hNp)\). Therefore
\[
\mathcal J(X):=
\det\frac{\partial(Y,Z,W)}{\partial(t,r,p)}
=\frac{r}{hNp}J(X)\in L^* .
\tag{27}
\]
In particular it is a nonzero polynomial of degree zero in X.
The coefficient partials in this determinant fix p. Replacing v
by a coefficient-dependent affine parameter is justified by the
full change-of-variables determinant in (27), not by silently
holding the old parameter fixed.

## 7. The full determinant excludes every possibility

Here is a direct exact expansion applicable to (24)--(26).
At fixed X the rows are
\[
\begin{aligned}
dY&=dy+X\,d\sigma+X^2dt,\\
dZ&=dz+X(2\sigma\,dt+2t\,d\sigma+dr)+2tX^2dt,\\
dW&=dw+X\,d\theta+
     X^2\left(\frac rh\,dr-\frac{r^2h'}{2h^2}dt\right).
\end{aligned}
\tag{28}
\]
Insert the displayed intercepts and take the coefficient of
\(dt\wedge dr\wedge dp\). Differentiation uses \(h'''=0\),
\(q'=q_1\), \(j'=j_1\). Before restricting epsilon to its two
allowed values, the two determinant identities are
\[
\begin{aligned}
\mathcal J_{\rm I}
 &=\frac{\varepsilon q_1^2h^2}{r^5}
       \left((2\varepsilon-1)Xr^2+2\varepsilon ph\right),\\
\mathcal J_{\rm II}
 &=\frac{\varepsilon q_1^2}{2r^3}
   \left(-8\varepsilon Xprh+(1-2\varepsilon)Xr^2h'
     +(8\varepsilon^2-4\varepsilon)q_1h^2+pr^2h''\right).
\end{aligned}
\tag{29}
\]
Thus these are full determinant identities, including the
constant coefficient and every X coefficient, not only leading
degree tests.

For \(\varepsilon=0\), both determinants in (29) are identically
zero, contradicting (27).

For \(\varepsilon=1\), their X coefficients are respectively
\[
[X]\mathcal J_{\rm I}=\frac{q_1^2h^2}{r^3}\ne0,\qquad
[X]\mathcal J_{\rm II}
 =-\frac{q_1^2}{2r^3}(8prh+r^2h').
\tag{30}
\]
The second expression is nonzero in \(L[p]\), since its
coefficient of the transcendental p is
\(-4q_1^2h/r^2\ne0\). Both contradict (27).
This last argument does not divide by \(h'\) and does not
evaluate at a specially chosen value of p or X.

All four combinations of direction and selected factor have
therefore been excluded. Under the retained actual reducible
projected-line hypotheses, \(m_s\ne0\) cannot occur.

## 8. Scope and verification boundary

The actual normalization, full kernel and selected derivation
are retained inputs from314. The new proof uses the full
factorization only to obtain the lower coefficient equations and
the actual unit factor difference. It does not assume that the
affine factor is the selected one.

The exact algebraic coefficient fields are retained until their
integration coefficients are proved complex. Neither an auxiliary
slice nor an invariant-coordinate theorem is used. The
contradiction is with the full literal calibrated determinant.
No leading-cancellation candidate is promoted to an ambient
identity.

Fresh unsaved symbolic calculations reconstructed the raw surface
from (3),(5), the complete lower coefficient chain, both selected
intercept families, and the entire determinants (29). They are
finite exact algebra checks; the field integrations, exhaustive
direction argument and actual calibration are the written proof.
No saved checker was executed, imported, compiled or rerun by
this author. No earlier source, checker, index or packet was
edited. No unrestricted cancellation or novelty claim is made.
